# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class CustomInfoCategory(models.Model):
    """
    Master-data model representing a category for grouping custom information
    properties.

    Categories are used to organise ``custom_info.property`` records on the
    custom-information template so that related properties are visually grouped
    together on the form view.
    """

    _description = "Categorize custom info properties"
    _name = "custom_info.category"
    _order = "sequence, name"

    name = fields.Char(
        string="Name",
        index=True,
        translate=True,
        required=True,
        help="Category name displayed on the form.",
    )
    code = fields.Char(
        string="Code",
        required=True,
        help="Unique short code identifying this category.",
    )
    sequence = fields.Integer(
        string="Sequence",
        index=True,
        default=5,
        help="Display order; lower value appears first.",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
        help="Inactive categories are hidden from menus.",
    )
    note = fields.Text(
        string="Note",
        help="Internal notes about this category.",
    )
