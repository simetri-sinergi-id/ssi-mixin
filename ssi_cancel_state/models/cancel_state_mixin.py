# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class CancelStateMixin(models.AbstractModel):
    _name = "cancel.state.mixin"
    _description = "Cancel State Mixin"

    cancel_reason_id = fields.Many2one(
        string="Cancel Reason",
        comodel_name="base.cancel.reason",
        readonly=True,
        copy=False,
    )
    reason = fields.Text(
        string="Cancellation Reason",
        copy=False,
    )
    cancel_date = fields.Datetime(
        string="Cancellation Date",
        readonly=True,
        copy=False,
    )
    cancel_user_id = fields.Many2one(
        string="Cancelled By",
        comodel_name="res.users",
        readonly=True,
        copy=False,
    )

    def action_cancel(self, cancel_reason, reason=""):
        for document in self:
            document.write(document._prepare_cancel_data(cancel_reason, reason))

    def _prepare_cancel_data(self, cancel_reason, reason):
        self.ensure_one()
        return {
            "cancel_reason_id": cancel_reason.id,
            "reason": reason,
            "cancel_date": fields.Datetime.now(),
            "cancel_user_id": self.env.user.id,
            "state": "cancel",
        }
