# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).
from odoo import fields, models


class DummyPolicyModel(models.Model):
    _name = "ssi.test.policy_mixin"
    _inherit = "mixin.policy"
    _description = "Dummy Policy Model"

    name = fields.Char(
        string="Name",
        required=True,
    )
    state = fields.Selection(
        string="State",
        selection=[("draft", "Draft"), ("confirmed", "Confirmed")],
        default="draft",
    )
    can_confirm = fields.Boolean(
        string="Can Confirm",
        compute="_compute_policy",
    )

    def _get_policy_field(self):
        return ["can_confirm"]
