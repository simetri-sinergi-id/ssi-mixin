# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class BaseTerminateReasonWizard(models.TransientModel):
    _name = "base.terminate.reason_wizard"
    _description = "Base Terminate Wizard"

    @api.model
    def _default_model_id(self):
        result = False
        model_name = self.env.context.get("active_model", False)
        if model_name:
            model = self.env["ir.model"].search([("model", "=", model_name)])[0]
            result = model.id
        return result

    @api.depends("configurator_id")
    def _compute_allowed_terminate_reason_ids(self):
        for document in self:
            result = []
            if document.configurator_id:
                result = document.configurator_id.terminate_reason_ids.ids
            document.allowed_terminate_reason_ids = result

    model_id = fields.Many2one(
        string="Model",
        comodel_name="ir.model",
        default=lambda self: self._default_model_id(),
    )
    configurator_id = fields.Many2one(
        string="Terminate Configurator",
        comodel_name="base.terminate.reason_config",
        required=True,
    )
    allowed_terminate_reason_ids = fields.Many2many(
        string="Allowed Terminate Reasons",
        comodel_name="base.terminate.reason",
        compute="_compute_allowed_terminate_reason_ids",
        store=False,
    )
    terminate_reason_id = fields.Many2one(
        string="Reason",
        comodel_name="base.terminate.reason",
        required=True,
    )
    type = fields.Selection(
        related="terminate_reason_id.type",
    )
    other_reason = fields.Text(
        string="Additional Explanation",
    )

    @api.onchange("model_id")
    def _onchange_configurator_id(self):
        obj_configurator = self.env["base.terminate.reason_config"]
        criteria = [
            ("name.id", "=", self.model_id.id),
        ]
        configurators = obj_configurator.search(criteria)
        if len(configurators) == 0:
            raise UserError(_("Error! No terminate configurator defined"))
        self.configurator_id = configurators[0]

    @api.model
    def _prepare_terminate_reason_data(self):
        reason = ""
        if self.type == "fixed":
            reason = self.terminate_reason_id.name
        else:
            reason = ("[%s] %s") % (self.terminate_reason_id.name, self.other_reason)
        return reason

    def action_confirm(self):
        for wiz in self:
            wiz._confirm_terminate()

    def _confirm_terminate(self):
        self.ensure_one()
        method_terminate_name = (
            self.configurator_id.method_terminate_name or "action_terminate"
        )
        obj_mixin = self.env[self.model_id.model]
        ids = self.env.context.get("active_ids", [])
        mixin = obj_mixin.search([("id", "in", ids)])
        if method_terminate_name and hasattr(mixin, method_terminate_name):
            method_terminate = getattr(mixin, method_terminate_name)
            other_reason = self._prepare_terminate_reason_data()
            method_terminate(self.terminate_reason_id, other_reason)
