# Copyright YYYY OpenSynergy Indonesia
# Copyright YYYY PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).
from odoo.exceptions import UserError
from odoo.tests.common import tagged

from .base import BaseCase


@tagged("post_install", "-at_install")
class TestMasterDataErrors(BaseCase):
    def test_create_with_invalid_integer_raises_value_error(self):
        """Membuat record dengan value integer tidak valid memunculkan ValueError."""
        with self.assertRaises(ValueError):
            self.test_model.with_user(self.test_user_1.id).create(
                {
                    "name": "Test",
                    "code": "TEST-002",
                    "value": "-",
                    "note": "Test Create Data",
                }
            )

    def test_generate_code_without_sequence_raises_user_error(self):
        """action_generate_code memunculkan UserError jika tidak ada template."""
        rec = self.test_model.with_user(self.test_user_1.id).create(
            {
                "name": "Test",
                "code": "TEST-003",
                "value": 10,
                "note": "Test",
            }
        )
        with self.assertRaises(UserError):
            rec.action_generate_code()
