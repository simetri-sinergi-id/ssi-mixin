# Copyright YYYY OpenSynergy Indonesia
# Copyright YYYY PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).
from odoo_test_helper import FakeModelLoader
from odoo_yaml_test import YamlTransactionCase

import odoo


class BaseCase(YamlTransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Create a multi-company
        cls.main_company = cls.env.ref("base.main_company")
        cls.other_company = cls.env["res.company"].create({"name": "My Company"})

        # Create users (do not depend on fake model):
        group_ids = cls.env.ref("base.group_system").ids
        cls.test_user_1 = cls.env["res.users"].create(
            {
                "name": "John",
                "login": "test1",
                "email": "john@yourcompany.example.com",
                "groups_id": [(6, 0, group_ids)],
            }
        )
        cls.test_user_2 = cls.env["res.users"].create(
            {"name": "Mike", "login": "test2", "email": "mike@yourcompany.example.com"}
        )
        cls.test_user_3_multi_company = cls.env["res.users"].create(
            {
                "name": "Jane",
                "login": "test3",
                "email": "jane@mycompany.example.com",
                "company_ids": [(6, 0, [cls.main_company.id, cls.other_company.id])],
            }
        )

    def setUp(self):
        super().setUp()
        self.loader = FakeModelLoader(self.env, self.__module__)
        self.loader.backup_registry()
        from .dummy_model import (
            DummyTestMasterData,
        )

        self.loader.update_registry((DummyTestMasterData,))
        self.test_model = self.env[DummyTestMasterData._name]

        # Buat model_id untuk dummy model
        self.tester_model = self.env["ir.model"].search(
            [("model", "=", DummyTestMasterData._name)]
        )

        # Buat field_id
        self.field_obj = self.env["ir.model.fields"].search(
            [("model_id", "=", self.tester_model.id), ("name", "=", "code")], limit=1
        )
        self.field_date_obj = self.env["ir.model.fields"].search(
            [
                ("model_id", "=", self.tester_model.id),
                ("ttype", "in", ["date", "datetime"]),
            ],
            limit=1,
        )

        for model in (self.tester_model,):
            self.env["ir.model.access"].create(
                {
                    "name": f"access {model.name}",
                    "model_id": model.id,
                    "perm_read": 1,
                    "perm_write": 1,
                    "perm_create": 1,
                    "perm_unlink": 1,
                }
            )

    def tearDown(self):
        from .dummy_model import DummyTestMasterData

        if "__annotations__" in DummyTestMasterData.__dict__:
            del DummyTestMasterData.__annotations__
        self.loader.restore_registry()
        super().tearDown()

    def _run_scenario(self, scenario, yaml_file):
        self.registry["tester_model"] = self.tester_model
        self.registry["field_obj"] = self.field_obj
        self.registry["field_date_obj"] = self.field_date_obj
        super()._run_scenario(scenario, yaml_file)

    def run_yaml_scenario(self, filename):
        real_registry = odoo.registry(self.env.cr.dbname)
        try:
            super().run_yaml_scenario(filename)
        finally:
            self.registry = real_registry
