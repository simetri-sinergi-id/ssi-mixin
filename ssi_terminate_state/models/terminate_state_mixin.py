# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class TerminateStateMixin(models.AbstractModel):
    _name = "terminate.state.mixin"
    _description = "Terminate State Mixin"

    terminate_reason_id = fields.Many2one(
        string="Terminate Reason",
        comodel_name="base.terminate.reason",
        readonly=True,
        copy=False,
    )
    terminate_reason = fields.Text(
        string="Terminate Reason",
        copy=False,
    )
    terminate_date = fields.Datetime(
        string="Terminate Date",
        readonly=True,
        copy=False,
    )
    terminate_user_id = fields.Many2one(
        string="Terminate By",
        comodel_name="res.users",
        readonly=True,
        copy=False,
    )

    def action_terminate(self, terminate_reason, reason=""):
        for document in self:
            document.write(document._prepare_terminate_data(terminate_reason, reason))

    def _prepare_terminate_data(self, terminate_reason, reason):
        self.ensure_one()
        return {
            "terminate_reason_id": terminate_reason.id,
            "terminate_reason": reason,
            "terminate_date": fields.Datetime.now(),
            "terminate_user_id": self.env.user.id,
            "state": "terminate",
        }
