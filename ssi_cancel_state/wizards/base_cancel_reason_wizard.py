# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class BaseCancelReasonWizard(models.TransientModel):
    _name = "base.cancel.reason_wizard"
    _description = "Base Cancel Wizard"

    @api.model
    def _default_model_id(self):
        result = False
        model_name = self.env.context.get("active_model", False)
        if model_name:
            model = self.env["ir.model"].search([("model", "=", model_name)])[0]
            result = model.id
        return result

    @api.depends("configurator_id")
    def _compute_allowed_cancel_reason_ids(self):
        for document in self:
            result = []
            if document.configurator_id:
                result = document.configurator_id.cancel_reason_ids.ids
            document.allowed_cancel_reason_ids = result

    model_id = fields.Many2one(
        string="Model",
        comodel_name="ir.model",
        default=lambda self: self._default_model_id(),
    )
    configurator_id = fields.Many2one(
        string="Cancel Configurator",
        comodel_name="base.cancel.reason_config",
        required=True,
    )
    allowed_cancel_reason_ids = fields.Many2many(
        string="Allowed Cancel Reasons",
        comodel_name="base.cancel.reason",
        compute="_compute_allowed_cancel_reason_ids",
        store=False,
    )
    cancel_reason_id = fields.Many2one(
        string="Reason",
        comodel_name="base.cancel.reason",
        required=True,
    )
    type = fields.Selection(
        related="cancel_reason_id.type",
    )
    other_reason = fields.Text(
        string="Additional Explanation",
    )

    @api.onchange("model_id")
    def _onchange_configurator_id(self):
        obj_configurator = self.env["base.cancel.reason_config"]
        criteria = [
            ("name.id", "=", self.model_id.id),
        ]
        configurators = obj_configurator.search(criteria)
        if len(configurators) == 0:
            raise UserError(_("Error! No cancel configurator defined"))
        self.configurator_id = configurators[0]

    def action_confirm(self):
        for wiz in self:
            wiz._confirm_cancel()

    def _confirm_cancel(self):
        self.ensure_one()
        method_cancel_name = self.configurator_id.method_cancel_name or "action_cancel"
        obj_mixin = self.env[self.model_id.model]
        ids = self.env.context.get("active_ids", [])
        mixin = obj_mixin.search([("id", "in", ids)])
        if method_cancel_name and hasattr(mixin, method_cancel_name):
            method_cancel = getattr(mixin, method_cancel_name)
            method_cancel(self.cancel_reason_id, self.other_reason)
