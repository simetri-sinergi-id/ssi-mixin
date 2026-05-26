# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).
from odoo_test_helper import FakeModelLoader

from odoo.tests import TransactionCase


class BaseCase(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Data yang tidak bergantung pada fake model — dibuat sekali
        group_ids = cls.env.ref("base.group_system").ids
        cls.test_user_1 = cls.env["res.users"].create(
            {
                "name": "John",
                "login": "test_tx_1",
                "email": "john@transaction.example.com",
                "groups_id": [(6, 0, group_ids)],
            }
        )
        cls.test_user_2 = cls.env["res.users"].create(
            {
                "name": "Mike",
                "login": "test_tx_2",
                "email": "mike@transaction.example.com",
            }
        )

    def setUp(self):
        super().setUp()
        self.loader = FakeModelLoader(self.env, self.__module__)
        self.loader.backup_registry()
        from .dummy_model import DummyTestTransaction

        self.loader.update_registry((DummyTestTransaction,))
        self.test_model = self.env[DummyTestTransaction._name]

        self.tester_model = self.env["ir.model"].search(
            [("model", "=", DummyTestTransaction._name)]
        )

        # Buat ir.model.access untuk dummy model
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
        from .dummy_model import DummyTestTransaction

        if "__annotations__" in DummyTestTransaction.__dict__:
            del DummyTestTransaction.__annotations__
        self.loader.restore_registry()
        super().tearDown()
