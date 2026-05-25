# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).
from odoo_test_helper import FakeModelLoader

from odoo.tests import TransactionCase


class BaseCase(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Create a multi-company
        cls.main_company = cls.env.ref("base.main_company")
        cls.other_company = cls.env["res.company"].create({"name": "My Company"})

        # Create users:
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

        # Buat sequence
        cls.sequence_1 = cls.env["ir.sequence"].create(
            {
                "name": "Test Sequence 1",
                "code": "ssi.test.sequence",
                "prefix": "TEST-1/",
                "number_next": 1,
                "number_increment": 1,
                "padding": 6,
            }
        )

        cls.sequence_2 = cls.env["ir.sequence"].create(
            {
                "name": "Test Sequence 2",
                "code": "ssi.test.sequence",
                "prefix": "TEST-2/",
                "number_next": 1,
                "number_increment": 1,
                "padding": 6,
            }
        )

    def setUp(self):
        super().setUp()
        self.loader = FakeModelLoader(self.env, self.__module__)
        self.loader.backup_registry()
        from .dummy_model import DummyTestSequence

        self.loader.update_registry((DummyTestSequence,))
        self.test_model = self.env[DummyTestSequence._name]

        # Buat model_id untuk dummy model
        self.tester_model = self.env["ir.model"].search(
            [("model", "=", "ssi.test.sequence")]
        )

        # Buat field_id
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

        # Access record:
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

        # Buat template sequence dengan python method
        self.template_python = self.env["sequence.template"].create(
            {
                "name": "Test Sequence Python",
                "model_id": self.tester_model.id,
                "sequence_field_id": self.field_obj.id,
                "date_field_id": self.field_date_obj.id,
                "initial_string": "/",
                "computation_method": "use_python",
                "python_code": (
                    "# env, document, result\n" "result = document.value > 10"
                ),
                "sequence_selection_method": "use_sequence",
                "sequence_id": self.sequence_1.id,
            }
        )

        # Buat template sequence dengan domain method
        self.template_domain = self.env["sequence.template"].create(
            {
                "name": "Test Sequence Domain",
                "model_id": self.tester_model.id,
                "sequence_field_id": self.field_obj.id,
                "date_field_id": self.field_date_obj.id,
                "initial_string": "/",
                "computation_method": "use_domain",
                "domain": "[('value', '<', 10)]",
                "sequence_selection_method": "use_sequence",
                "sequence_id": self.sequence_2.id,
            }
        )

    def tearDown(self):
        self.loader.restore_registry()
        super().tearDown()
