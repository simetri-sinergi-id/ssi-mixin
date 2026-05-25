# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0.html).

from odoo import _, api, fields, models
from odoo.exceptions import UserError
from odoo.tools.safe_eval import safe_eval


class MixinPolicy(models.AbstractModel):
    """
    Mixin object for workflow policy extensibility.
    """

    _name = "mixin.policy"
    _description = "Mixin Object for Workflow Policy"

    @api.model
    def _get_policy_field(self):
        """
        Return list of policy fields for extensibility.
        """
        return []

    def _compute_allowed_policy_template_ids(self):
        """
        Compute allowed policy templates for this model.
        """
        obj_template = self.env["policy.template"]
        for record in self:
            criteria = [
                ("model", "=", self._name),
            ]
            record.allowed_policy_template_ids = obj_template.search(criteria).ids

    allowed_policy_template_ids = fields.Many2many(
        string="Allowed Policy Templates",
        comodel_name="policy.template",
        compute="_compute_allowed_policy_template_ids",
        store=False,
        help="Allowed policy templates for this record.",
    )
    policy_template_id = fields.Many2one(
        string="Policy Template",
        comodel_name="policy.template",
        copy=False,
        domain=lambda self: [("model", "=", self._name)],
        help="Policy template applied to this record.",
    )

    def _get_policy_localdict(self):
        """
        Get localdict for policy evaluation.
        """
        self.ensure_one()
        return {
            "env": self.env,
            "document": self,
        }

    def _evaluate_policy(self, template):
        """
        Evaluate policy python code safely.
        """
        self.ensure_one()
        res = False
        localdict = self._get_policy_localdict()
        try:
            safe_eval(template.python_code, localdict, mode="exec", nocopy=True)
            res = localdict["result"]
        except Exception as error:
            raise UserError(_(f"Error evaluating conditions.\n {error}")) from error
        return res

    def _get_template_policy(self):
        """
        Get template policy for this record.
        """
        self.ensure_one()
        result = False
        obj_policy_template = self.env["policy.template"]
        criteria = [
            ("model_id.model", "=", str(self._name)),
        ]
        policy_templates = obj_policy_template.search(
            criteria,
            order="sequence desc",
        )
        for template in policy_templates:
            if self._evaluate_policy(template):
                result = template.id
                break
        return result

    def action_reload_policy_template(self):
        for record in self:
            record.write(
                {
                    "policy_template_id": record._get_template_policy(),
                }
            )

    def _prepare_policy_field_data(self):
        data = {}
        policy_field = self._get_policy_field()
        if policy_field:
            for policy in policy_field:
                data[policy] = False
        return data

    @api.depends(
        "policy_template_id",
    )
    def _compute_policy(self):
        for document in self:
            data = document._prepare_policy_field_data()
            if document.policy_template_id:
                for detail in document.policy_template_id.detail_ids:
                    result = detail.get_policy(document)
                    data[detail.field_id.name] = result
            for key in data:
                setattr(
                    document,
                    key,
                    data.get(key),
                )

    @api.model
    def create(self, values):
        _super = super()
        result = _super.create(values)
        if not result.policy_template_id:
            template_id = result._get_template_policy()
            if template_id:
                result.write({"policy_template_id": template_id})
        return result
