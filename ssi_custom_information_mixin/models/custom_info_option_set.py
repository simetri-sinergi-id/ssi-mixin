# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class CustomInfoOptionSet(models.Model):
    """
    A named collection of ``custom_info.option`` records that can be
    referenced by one or more ``custom_info.property`` records of type
    ``Selection`` or ``Multiple Selection``.

    Sharing an option set across multiple properties avoids duplicating the
    option list and ensures consistent vocabulary.
    """

    _description = "Option Sets for Custom Information"
    _name = "custom_info.option_set"

    name = fields.Char(
        string="Name",
        index=True,
        translate=True,
        required=True,
        help="Option set name.",
    )
    code = fields.Char(
        string="Code",
        required=True,
        help="Unique short code identifying this option set.",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
        help="Inactive option sets are hidden from selection.",
    )
    note = fields.Text(
        string="Note",
        help="Internal notes about this option set.",
    )
    option_ids = fields.Many2many(
        string="Options",
        comodel_name="custom_info.option",
        relation="rel_option_set_2_option",
        column1="set_id",
        column2="option_id",
        help="Options that belong to this set.",
    )
