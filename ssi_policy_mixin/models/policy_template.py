# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0.html).

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import test_python_expr


class PolicyTemplate(models.Model):
    """
    Policy Template model for reusable workflow and business rules.
    """

    _name = "policy.template"
    _description = "Policy Template"
    _order = "sequence, id"

    DEFAULT_PYTHON_CODE = """# Available variables:\n"
        "#  - env: Odoo Environment on which the action is triggered.\n"
        "#  - document: record on which the action is triggered; may be void.\n"
        "#  - result: Return result, the value is boolean.\n"""

    @api.model
    def _default_company_id(self):
        """
        Get default company for policy template.
        """
        return self.env["res.company"]._company_default_get("policy.template")

    name = fields.Char(
        string="Name", required=True, copy=True, help="Policy template name."
    )
    model_id = fields.Many2one(
        string="Referenced Model",
        comodel_name="ir.model",
        ondelete="cascade",
        index=True,
        required=True,
        copy=True,
        help="Model to which this policy applies.",
    )
    model = fields.Char(
        related="model_id.model", index=True, store=True, help="Technical model name."
    )
    state_field_id = fields.Many2one(
        string="State Field",
        comodel_name="ir.model.fields",
        domain="[('ttype', '=', 'selection'), ('model_id', '=', model_id)]",
        copy=True,
        help="State field for workflow restriction.",
    )
    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        default=lambda self: self._default_company_id(),
        copy=True,
        help="Company for which this policy is valid.",
    )
    sequence = fields.Integer(
        default=5, required=True, copy=True, help="Sequence for ordering."
    )
    active = fields.Boolean(
        default=True,
        help="If unchecked, the policy is inactive.",
        copy=True,
    )
    note = fields.Text(
        string="Note",
        copy=True,
    )
    detail_ids = fields.One2many(
        string="Details",
        comodel_name="policy.template_detail",
        inverse_name="template_id",
        copy=True,
    )
    domain = fields.Char(
        string="Domain",
        copy=True,
    )
    python_code = fields.Text(
        string="Python Code",
        default=DEFAULT_PYTHON_CODE,
        copy=True,
    )

    def name_get(self):
        result = []
        for record in self:
            name = f"[{record.model}] {record.name}"
            result.append((record.id, name))
        return result

    @api.constrains(
        "python_code",
    )
    def _check_python_code(self):
        for action in self.sudo().filtered("python_code"):
            msg = test_python_expr(expr=action.python_code.strip(), mode="exec")
            if msg:
                msg1 = "Template:\n"
                raise ValidationError(msg1 + msg)
