# Copyright YYYY OpenSynergy Indonesia
# Copyright YYYY PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).
from odoo.exceptions import UserError
from odoo.tests.common import tagged

from .base import BaseCase


@tagged("post_install", "-at_install")
class TestDuplicateCode(BaseCase):
    def test_create_duplicate_code_raises_user_error(self):
        """Membuat record dengan code yang sama memunculkan UserError."""
        self.test_model.with_user(self.test_user_1.id).create(
            {
                "name": "Test 1",
                "code": "TEST-001",
                "value": 10,
                "note": "First record",
            }
        )
        with self.assertRaises(UserError):
            self.test_model.with_user(self.test_user_1.id).create(
                {
                    "name": "Test 2",
                    "code": "TEST-001",
                    "value": 20,
                    "note": "Second record",
                }
            )
