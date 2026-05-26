# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).
from odoo_test_helper import FakeModelLoader

from odoo.tests import TransactionCase


class BaseCase(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

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
            {
                "name": "Mike",
                "login": "test2",
                "email": "mike@yourcompany.example.com",
            }
        )

    def setUp(self):
        super().setUp()
        self.loader = FakeModelLoader(self.env, self.__module__)
        self.loader.backup_registry()
        from .dummy_model import (
            DummyPolicyModel,
        )

        self.loader.update_registry((DummyPolicyModel,))
        self.test_model = self.env[DummyPolicyModel._name]

        # Buat model_id untuk dummy model
        self.tester_model = self.env["ir.model"].search(
            [("model", "=", "ssi.test.policy_mixin")]
        )

        # Buat field_id untuk field can_confirm
        self.can_confirm_field = self.env["ir.model.fields"].search(
            [("model_id", "=", self.tester_model.id), ("name", "=", "can_confirm")],
            limit=1,
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
        self.loader.restore_registry()
        super().tearDown()
