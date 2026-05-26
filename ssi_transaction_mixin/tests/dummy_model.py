# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).
from odoo import fields, models


class DummyTestTransaction(models.Model):
    _name = "ssi.test.transaction_mixin"
    _inherit = "mixin.transaction"
    _description = "Dummy Test Transaction"

    state = fields.Selection(
        selection_add=[
            ("confirmed", "Confirmed"),
        ],
        ondelete={"confirmed": "set default"},
    )

    def _get_policy_field(self):
        res = super()._get_policy_field()
        return res + ["restart_ok", "manual_number_ok"]
