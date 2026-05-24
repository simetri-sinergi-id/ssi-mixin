# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class CustomInfoOption(models.Model):
    """
    A single selectable value for a custom information property of type
    ``Selection`` or ``Multiple Selection``.

    Options are grouped into ``custom_info.option_set`` records, which are
    then attached to ``custom_info.property`` records that require a
    controlled vocabulary.
    """

    _description = "Available options for a custom property"
    _name = "custom_info.option"
    _order = "name"

    name = fields.Char(
        string="Name",
        index=True,
        translate=True,
        required=True,
        help="Option label shown to the user.",
    )
    code = fields.Char(
        string="Code",
        required=True,
        help="Unique short code identifying this option.",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
        help="Inactive options are hidden from selection lists.",
    )
    note = fields.Text(
        string="Note",
        help="Internal notes about this option.",
    )
