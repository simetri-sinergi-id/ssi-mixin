# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).
from odoo.exceptions import UserError
from odoo.tests.common import tagged

from .base import BaseCase


@tagged("post_install", "-at_install")
class TestSequenceErrors(BaseCase):
    def test_no_template_raises_user_error(self):
        """_create_sequence raises UserError when no matching template exists."""
        doc = self.test_model.with_user(self.test_user_1.id).create(
            {"name": "/", "value": 999}
        )
        # Tidak ada template yang di-setup → UserError dengan pesan tentang template
        with self.assertRaises(UserError):
            doc._create_sequence()

    def test_invalid_prefix_code_raises_user_error(self):
        """_create_sequence raises UserError when prefix_python_code is invalid."""
        ir_seq = self.env["ir.sequence"].create(
            {
                "name": "Test Seq - Invalid Prefix",
                "code": "ssi.test.seq.invalid.prefix",
                "number_next": 1,
                "number_increment": 1,
                "padding": 6,
            }
        )
        self.env["sequence.template"].create(
            {
                "name": "Template - Invalid Prefix Code",
                "model_id": self.tester_model.id,
                "sequence_field_id": self.field_obj.id,
                "date_field_id": self.field_date_obj.id,
                "initial_string": "/",
                "computation_method": "use_python",
                "python_code": "result = True",
                "sequence_selection_method": "use_sequence",
                "sequence_id": ir_seq.id,
                "add_custom_prefix": True,
                # Invalid Python: "-" is not a statement that sets localdict["result"],
                # causing safe_eval to raise SyntaxError → caught → UserError
                "prefix_python_code": "-",
                "sequence": 1000,
            }
        )
        doc = self.test_model.with_user(self.test_user_1.id).create(
            {"name": "/", "value": 15}
        )
        with self.assertRaises(UserError):
            doc._create_sequence()

    def test_invalid_suffix_code_raises_user_error(self):
        """_create_sequence raises UserError when suffix_python_code is invalid."""
        ir_seq = self.env["ir.sequence"].create(
            {
                "name": "Test Seq - Invalid Suffix",
                "code": "ssi.test.seq.invalid.suffix",
                "number_next": 1,
                "number_increment": 1,
                "padding": 6,
            }
        )
        self.env["sequence.template"].create(
            {
                "name": "Template - Invalid Suffix Code",
                "model_id": self.tester_model.id,
                "sequence_field_id": self.field_obj.id,
                "date_field_id": self.field_date_obj.id,
                "initial_string": "/",
                "computation_method": "use_python",
                "python_code": "result = True",
                "sequence_selection_method": "use_sequence",
                "sequence_id": ir_seq.id,
                "add_custom_suffix": True,
                # Invalid Python: "-" triggers SyntaxError in safe_eval → UserError
                "suffix_python_code": "-",
                "sequence": 1000,
            }
        )
        doc = self.test_model.with_user(self.test_user_1.id).create(
            {"name": "/", "value": 15}
        )
        with self.assertRaises(UserError):
            doc._create_sequence()

    def test_python_condition_false_falls_through_to_next_template(self):
        """When python_code returns False, the next template in order is evaluated."""
        ir_seq_domain = self.env["ir.sequence"].create(
            {
                "name": "Test Seq - Domain Fallthrough",
                "code": "ssi.test.seq.domain.fall",
                "prefix": "FALL/",
                "number_next": 1,
                "number_increment": 1,
                "padding": 6,
            }
        )
        # Template Python (sequence=100): condition always False
        ir_seq_python = self.env["ir.sequence"].create(
            {
                "name": "Test Seq - Python False",
                "code": "ssi.test.seq.python.false",
                "prefix": "NEVER/",
                "number_next": 1,
                "number_increment": 1,
                "padding": 6,
            }
        )
        self.env["sequence.template"].create(
            {
                "name": "Template - Python Always False",
                "model_id": self.tester_model.id,
                "sequence_field_id": self.field_obj.id,
                "date_field_id": self.field_date_obj.id,
                "initial_string": "/",
                "computation_method": "use_python",
                "python_code": "result = False",
                "sequence_selection_method": "use_sequence",
                "sequence_id": ir_seq_python.id,
                "sequence": 100,
            }
        )
        # Template Domain (sequence=10): condition True for value < 100
        self.env["sequence.template"].create(
            {
                "name": "Template - Domain Fallthrough",
                "model_id": self.tester_model.id,
                "sequence_field_id": self.field_obj.id,
                "date_field_id": self.field_date_obj.id,
                "initial_string": "/",
                "computation_method": "use_domain",
                "domain": "[('value', '<', 100)]",
                "sequence_selection_method": "use_sequence",
                "sequence_id": ir_seq_domain.id,
                "sequence": 10,
            }
        )
        doc = self.test_model.with_user(self.test_user_1.id).create(
            {"name": "/", "value": 50}
        )
        doc._create_sequence()
        # NEVER/ template skipped; FALL/ domain template used
        self.assertIn("FALL/", doc.name)
        self.assertNotIn("NEVER/", doc.name)
