# Copyright 2018 Eficent Business and IT Consulting Services S.L.
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class TierDefinition(models.Model):
    _name = "tier.definition"
    _description = "Tier Definition"
    _order = "sequence, id"

    def _compute_allowed_model_ids(self):
        obj_model = self.env["tier.definition_reference_model"]
        for record in self:
            record.allowed_model_ids = obj_model.search([]).mapped("model_id.id")

    name = fields.Char(
        string="Name",
        required=True,
    )
    allowed_model_ids = fields.Many2many(
        string="Allowed Models",
        comodel_name="ir.model",
        compute="_compute_allowed_model_ids",
        store=False,
    )
    model_id = fields.Many2one(
        string="Referenced Model",
        comodel_name="ir.model",
    )
    model = fields.Char(
        related="model_id.model",
        index=True,
        store=True,
    )
    python_code = fields.Text(
        string="Tier Definition Expression",
        help="Write Python code that defines when this tier confirmation "
        "will be needed. The result of executing the expresion must be "
        "a boolean.",
        default="""# Available locals:\n#  - rec: current record""",
    )
    sequence = fields.Integer(
        default=1,
        required=True,
    )
    active = fields.Boolean(
        default=True,
    )
    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        default=lambda self: self.env.company,
    )
    definition_review_ids = fields.One2many(
        string="Reviewer(s)",
        comodel_name="tier.definition.review",
        inverse_name="definition_id",
    )
    validate_sequence = fields.Boolean(
        string="Validate by Sequence",
        help="Validation by reviewer must be done by sequence.",
    )
    special_validation = fields.Boolean(
        string="Special Validation",
        help="This validation can only be selected manually. ",
    )
    notify_on_create = fields.Boolean(
        string="Notify Reviewers on Creation",
        help="If set, all possible reviewers will be notified by email when "
        "this definition is triggered.",
    )
