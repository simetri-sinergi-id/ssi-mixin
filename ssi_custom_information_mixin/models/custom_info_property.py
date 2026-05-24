# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class CustomInfoProperty(models.Model):
    """
    Defines a single custom-information property: its name, code, data type
    (text, integer, decimal, boolean, selection, multiple-selection, date, or
    datetime), and an optional option set for selection-type properties.

    Properties are assigned to models through ``custom_info.template_detail``
    records on a ``custom_info.template``.
    """

    _description = "Custom information property"
    _name = "custom_info.property"

    name = fields.Char(
        string="Name",
        required=True,
        translate=True,
        help="Property name shown to the user.",
    )
    code = fields.Char(
        string="Code",
        required=True,
        help="Unique short code identifying this property.",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
        help="Inactive properties are hidden from templates.",
    )
    note = fields.Text(
        string="Note",
        help="Internal notes about this property.",
    )
    field_type = fields.Selection(
        string="Field Type",
        selection=[
            ("str", "Text"),
            ("int", "Whole number"),
            ("float", "Decimal number"),
            ("bool", "Yes/No"),
            ("id", "Selection"),
            ("ids", "Multiple Selection"),
            ("date", "Date"),
            ("datetime", "Datetime"),
        ],
        default="str",
        required=True,
        help="Data type for the property value.",
    )
    option_set_id = fields.Many2one(
        string="Option Set",
        comodel_name="custom_info.option_set",
        help="Option set used for selection-type properties.",
    )
    option_ids = fields.Many2many(
        string="Options",
        comodel_name="custom_info.option",
        related="option_set_id.option_ids",
        store=False,
        readonly=True,
        help="Available options, derived from the selected option set.",
    )
