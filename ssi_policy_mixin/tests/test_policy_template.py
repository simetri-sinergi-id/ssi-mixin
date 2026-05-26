# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).
from odoo.exceptions import ValidationError
from odoo.tests.common import tagged

from .base import BaseCase


@tagged("post_install", "-at_install")
class TestPolicyTemplate(BaseCase):
    def _create_template(self, name="Test Template", python_code="result = True"):
        return self.env["policy.template"].create(
            {
                "name": name,
                "model_id": self.tester_model.id,
                "python_code": python_code,
            }
        )

    def test_create_valid(self):
        template = self._create_template()
        self.assertEqual(template.name, "Test Template")
        self.assertEqual(template.model_id, self.tester_model)

    def test_name_get(self):
        template = self._create_template()
        name = template.name_get()
        self.assertIn(self.tester_model.model, name[0][1])
        self.assertIn("Test Template", name[0][1])

    def test_invalid_python_code(self):
        with self.assertRaises(ValidationError):
            self._create_template(python_code="this is not !!! valid python")

    def test_invalid_detail_python_code(self):
        template = self._create_template()
        with self.assertRaises(ValidationError):
            self.env["policy.template_detail"].create(
                {
                    "template_id": template.id,
                    "field_id": self.can_confirm_field.id,
                    "restrict_state": False,
                    "restrict_user": True,
                    "computation_method": "use_python",
                    "python_code": "this is not !!! valid python",
                }
            )
