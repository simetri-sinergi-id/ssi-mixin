# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID, api, fields, models
from odoo.tools.safe_eval import safe_eval as eval


class BasePrintDocument(models.TransientModel):
    _name = "base.print.document"
    _description = "Base Print Document"

    @api.model
    def _compute_allowed_print_action_ids(self):
        result = []
        obj_print_policy = self.env["base.print.policy"]
        active_model = self.env.context.get("active_model", "")
        criteria = [("report_action_id.model", "=", active_model)]
        print_policy_ids = obj_print_policy.search(criteria)
        if print_policy_ids:
            for print_policy in print_policy_ids:
                allowed_print = self._check_allowed_print(print_policy)
                if allowed_print:
                    policy = self.get_print_policy(print_policy.python_condition)
                    if policy:
                        result.append(print_policy.report_action_id.id)
        return result

    allowed_print_action_ids = fields.Many2many(
        string="Allowed Print Action",
        comodel_name="ir.actions.report",
        default=lambda self: self._compute_allowed_print_action_ids(),
        relation="rel_print_document_2_action_report",
        column1="wizard_id",
        column2="report_action_id",
    )

    report_action_id = fields.Many2one(
        string="Report Template",
        comodel_name="ir.actions.report",
        required=True,
    )

    def _check_allowed_print(self, object):
        user = self.env.user
        if user.id == SUPERUSER_ID:
            result = True
        else:
            if object.group_ids:
                user_group_ids = user.groups_id.ids
                if set(object.group_ids.ids) & set(user_group_ids):
                    result = True
                else:
                    result = False
            else:
                result = True
        return result

    def _get_object(self):
        active_id = self.env.context.get("active_id", False)
        active_model = self.env.context.get("active_model", "")
        # TODO: Assert when invalid active_id or active_model
        object = self.env[active_model].browse([active_id])[0]
        return object

    def _get_localdict(self):
        return {"record": self._get_object()}

    def get_print_policy(self, python_condition):
        localdict = self._get_localdict()

        try:
            eval(python_condition, localdict, mode="exec", nocopy=True)
            result = localdict["result"]
        except Exception:
            result = True

        return result

    def action_print(self):
        res = False
        obj_report = self.env["ir.actions.report"]
        object = self._get_object()
        report_name = self.report_action_id.report_name
        criteria = [("report_name", "=", report_name)]
        report = obj_report.search(criteria, limit=1)
        if report:
            res = report.report_action(object)
        return res
