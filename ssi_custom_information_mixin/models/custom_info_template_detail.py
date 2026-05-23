# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class CustomInfoTemplateDetail(models.Model):
    """
    Child record linking a ``custom_info.property`` to a
    ``custom_info.template``, optionally grouped by a
    ``custom_info.category``.

    A unique constraint prevents the same property from appearing more than
    once on a template.
    """

    _description = "Custom Information Template Detail"
    _name = "custom_info.template_detail"
    _order = "template_id, property_id"
    _sql_constraints = [
        (
            "template_property",
            "UNIQUE (template_id, property_id)",
            "Another Property with that name exists for that Template.",
        ),
    ]

    template_id = fields.Many2one(
        string="Template",
        comodel_name="custom_info.template",
        required=True,
        ondelete="cascade",
        help="Template this detail belongs to.",
    )
    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=1,
        help="Display order within the template.",
    )
    property_id = fields.Many2one(
        string="Property",
        comodel_name="custom_info.property",
        required=True,
        help="Custom property included in this template.",
    )
    category_id = fields.Many2one(
        string="Category",
        comodel_name="custom_info.category",
        help="Optional category to group this property on the form.",
    )
