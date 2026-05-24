# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import test_python_expr


class CustomInfoTemplate(models.Model):
    _description = "Custom information template"
    _name = "custom_info.template"
    _order = "model_id, name"
    _sql_constraints = [
        (
            "name_model",
            "UNIQUE (name, model_id)",
            "Another template with that name exists for that model.",
        ),
    ]

    DEFAULT_PYTHON_CODE = """# Available variables:
#  - env: Odoo Environment on which the action is triggered.
#  - document: record on which the action is triggered; may be void."""

    name = fields.Char(
        string="Name",
        required=True,
        translate=True,
        help="Template name.",
    )
    model_id = fields.Many2one(
        string="Referenced Model",
        comodel_name="ir.model",
        ondelete="cascade",
        index=True,
        required=True,
        help="Odoo model this template applies to.",
    )
    model = fields.Char(
        related="model_id.model",
        index=True,
        store=True,
        help="Technical model name (auto-filled).",
    )

    @api.model
    def _default_company_id(self):
        return self.env.company

    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        default=lambda self: self._default_company_id(),
        help="Company this template belongs to.",
    )
    sequence = fields.Integer(
        string="Sequence",
        default=1,
        required=True,
        help="Determines evaluation order; higher sequence = lower priority.",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
        help="Inactive templates are hidden but not deleted.",
    )
    note = fields.Text(
        string="Note",
        help="Internal notes about this template.",
    )
    computation_method = fields.Selection(
        string="Computation Method",
        selection=[
            ("use_domain", "Domain"),
            ("use_python", "Python Code"),
        ],
        default="use_python",
        required=True,
        help="Method used to determine whether this template applies to a record.",
    )
    domain = fields.Char(
        string="Domain",
        help="Domain filter to match records (used when computation method is Domain).",
    )
    python_code = fields.Text(
        string="Python Code",
        default=DEFAULT_PYTHON_CODE
        + "\n#  - result: Return result, the value is boolean.",
        copy=True,
        help="Python code to evaluate applicability "
        "(used when computation method is Python Code).",
    )
    detail_ids = fields.One2many(
        string="Details",
        comodel_name="custom_info.template_detail",
        inverse_name="template_id",
        help="Properties included in this template.",
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
                raise ValidationError(msg)
