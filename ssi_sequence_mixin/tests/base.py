# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).
from odoo_test_helper import FakeModelLoader
from odoo_yaml_test import YamlTransactionCase


class BaseCase(YamlTransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Data yang tidak bergantung pada fake model — dibuat sekali
        # untuk semua test method
        group_ids = cls.env.ref("base.group_system").ids
        cls.test_user_1 = cls.env["res.users"].create(
            {
                "name": "John",
                "login": "test_seq_1",
                "email": "john@seq.example.com",
                "groups_id": [(6, 0, group_ids)],
            }
        )
        cls.test_user_2 = cls.env["res.users"].create(
            {
                "name": "Mike",
                "login": "test_seq_2",
                "email": "mike@seq.example.com",
            }
        )

    def setUp(self):
        super().setUp()
        # FakeModelLoader wajib di setUp agar restore_registry berjalan
        # sebelum check_attrs
        self.loader = FakeModelLoader(self.env, self.__module__)
        self.loader.backup_registry()
        from .dummy_model import DummyTestSequence

        self.loader.update_registry((DummyTestSequence,))
        self.test_model = self.env[DummyTestSequence._name]

        # Cari ir.model dan ir.model.fields untuk dummy model
        self.tester_model = self.env["ir.model"].search(
            [("model", "=", DummyTestSequence._name)]
        )
        self.field_obj = self.env["ir.model.fields"].search(
            [("model_id", "=", self.tester_model.id), ("name", "=", "name")], limit=1
        )
        self.field_date_obj = self.env["ir.model.fields"].search(
            [
                ("model_id", "=", self.tester_model.id),
                ("ttype", "in", ["date", "datetime"]),
            ],
            limit=1,
        )

        # Buat access record untuk dummy model
        self.env["ir.model.access"].create(
            {
                "name": f"access {self.tester_model.name}",
                "model_id": self.tester_model.id,
                "perm_read": 1,
                "perm_write": 1,
                "perm_create": 1,
                "perm_unlink": 1,
            }
        )

    def tearDown(self):
        self.loader.restore_registry()
        super().tearDown()

    def run_yaml_scenario(self, filename):
        """Wrap run_yaml_scenario to restore self.registry to the Odoo ORM
        registry after each call.

        YamlTransactionCase.setUp() overwrites self.registry with {}, then
        each scenario leaves it populated with recordsets. Odoo 18+ CI builds
        include a check_attrs() hook (run via doCleanups) that iterates over
        self.registry.values() and calls vars(model) on each item. Odoo
        recordsets define __slots__ = () and therefore have no __dict__, so
        vars() raises TypeError. Restoring self.registry here ensures
        check_attrs sees the real Odoo ORM registry (containing model classes)
        rather than the scenario's recordset dict.
        """
        import odoo

        real_registry = odoo.registry(self.env.cr.dbname)
        try:
            super().run_yaml_scenario(filename)
        finally:
            self.registry = real_registry
