# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class BaseTerminateReason(models.Model):
    _name = "base.terminate.reason"
    _description = "Base Terminate Reason"

    name = fields.Char(
        string="Terminate Reason",
        required=True,
    )
    type = fields.Selection(
        string="Type",
        selection=[
            ("fixed", "Fixed"),
            ("not_fixed", "Need more explanation"),
        ],
        default="fixed",
        required=True,
    )
    default = fields.Boolean(
        string="Create as Default",
        default=False,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    description = fields.Text(
        string="Note",
    )
