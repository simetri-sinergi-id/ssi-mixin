# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).
from odoo.exceptions import UserError
from odoo.tests.common import tagged

from .base import BaseCase


@tagged("post_install", "-at_install")
class TestPolicyMixin(BaseCase):
    def _create_template(self, python_code="result = True"):
        return self.env["policy.template"].create(
            {
                "name": "Test Template",
                "model_id": self.tester_model.id,
                "python_code": python_code,
            }
        )

    def _create_detail(
        self,
        template,
        computation_method="use_python",
        python_code="result = True",
        user_ids=None,
    ):
        vals = {
            "template_id": template.id,
            "field_id": self.can_confirm_field.id,
            "restrict_state": False,
            "restrict_user": True,
            "computation_method": computation_method,
        }
        if computation_method == "use_python":
            vals["python_code"] = python_code
        if computation_method == "use_user" and user_ids:
            vals["user_ids"] = [(6, 0, user_ids)]
        if computation_method == "use_group":
            vals["group_ids"] = [(6, 0, user_ids or [])]
        return self.env["policy.template_detail"].create(vals)

    def test_get_template_policy_no_template(self):
        record = self.test_model.with_user(self.test_user_1.id).create(
            {"name": "Rec 1"}
        )
        result = record._get_template_policy()
        self.assertFalse(result)

    def test_get_template_policy_match(self):
        template = self._create_template("result = True")
        record = self.test_model.with_user(self.test_user_1.id).create(
            {"name": "Rec 1"}
        )
        result = record._get_template_policy()
        self.assertEqual(result, template.id)

    def test_get_template_policy_no_match(self):
        self._create_template("result = False")
        record = self.test_model.with_user(self.test_user_1.id).create(
            {"name": "Rec 1"}
        )
        result = record._get_template_policy()
        self.assertFalse(result)

    def test_evaluate_policy_true(self):
        template = self._create_template("result = True")
        record = self.test_model.with_user(self.test_user_1.id).create(
            {"name": "Rec 1"}
        )
        self.assertTrue(record._evaluate_policy(template))

    def test_evaluate_policy_false(self):
        template = self._create_template("result = False")
        record = self.test_model.with_user(self.test_user_1.id).create(
            {"name": "Rec 1"}
        )
        self.assertFalse(record._evaluate_policy(template))

    def test_evaluate_policy_error(self):
        # Create record first so create() does not trigger evaluation on bad template
        record = self.test_model.with_user(self.test_user_1.id).create(
            {"name": "Rec 1"}
        )
        # result = 1/0 has valid syntax but raises ZeroDivisionError at runtime
        template = self._create_template("result = 1/0")
        with self.assertRaises(UserError):
            record._evaluate_policy(template)

    def test_action_reload_policy_template(self):
        template = self._create_template("result = True")
        record = self.test_model.with_user(self.test_user_1.id).create(
            {"name": "Rec 1"}
        )
        record.policy_template_id = False
        record.action_reload_policy_template()
        self.assertEqual(record.policy_template_id.id, template.id)

    def test_compute_policy_use_python_allowed(self):
        template = self._create_template("result = True")
        self._create_detail(
            template, computation_method="use_python", python_code="result = True"
        )
        record = self.test_model.with_user(self.test_user_1.id).create(
            {"name": "Rec 1"}
        )
        record.write({"policy_template_id": template.id})
        self.assertTrue(record.with_user(self.test_user_1.id).can_confirm)

    def test_compute_policy_use_python_denied(self):
        template = self._create_template("result = True")
        self._create_detail(
            template, computation_method="use_python", python_code="result = False"
        )
        record = self.test_model.with_user(self.test_user_1.id).create(
            {"name": "Rec 1"}
        )
        record.write({"policy_template_id": template.id})
        self.assertFalse(record.with_user(self.test_user_1.id).can_confirm)

    def test_compute_policy_use_user_allowed(self):
        template = self._create_template("result = True")
        self._create_detail(
            template,
            computation_method="use_user",
            user_ids=[self.test_user_1.id],
        )
        record = self.test_model.with_user(self.test_user_1.id).create(
            {"name": "Rec 1"}
        )
        record.write({"policy_template_id": template.id})
        # Test detail.get_policy() directly with user_1 (in user_ids) → True
        result = False
        for detail in record.policy_template_id.detail_ids:
            result = detail.with_user(self.test_user_1.id).get_policy(record)
        self.assertTrue(result)

    def test_compute_policy_use_user_denied(self):
        template = self._create_template("result = True")
        self._create_detail(
            template,
            computation_method="use_user",
            user_ids=[self.test_user_1.id],
        )
        # Create record as user_1 (has system access to search policy.template)
        record = self.test_model.with_user(self.test_user_1.id).create(
            {"name": "Rec 1"}
        )
        record.write({"policy_template_id": template.id})
        # Test detail.get_policy() directly with user_2 (NOT in user_ids) → False
        result = False
        for detail in record.policy_template_id.detail_ids:
            result = detail.with_user(self.test_user_2.id).get_policy(record)
        self.assertFalse(result)

    def test_compute_policy_no_template(self):
        record = self.test_model.with_user(self.test_user_1.id).create(
            {"name": "Rec 1"}
        )
        self.assertFalse(record.can_confirm)
