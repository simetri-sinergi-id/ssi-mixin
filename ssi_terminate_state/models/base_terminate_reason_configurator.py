# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class BaseTerminateReasonConfigurator(models.Model):
    _name = "base.terminate.reason_config"
    _description = "Base Terminate Reason Configurator"

    name = fields.Many2one(
        string="Model",
        comodel_name="ir.model",
    )
    method_terminate_name = fields.Char(string="Method Terminate Name")
    terminate_reason_ids = fields.Many2many(
        string="Terminate Reason",
        comodel_name="base.terminate.reason",
        relation="base_terminate_reason_config_rel",
        column1="config_id",
        column2="reason_id",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    description = fields.Text(
        string="Note",
    )

    @api.model
    def _get_default_reason_ids(self):
        result = False
        obj_terminate_reason = self.env["base.terminate.reason"]
        criteria = [("default", "=", True)]
        terminate_reason_ids = obj_terminate_reason.search(criteria)
        if terminate_reason_ids:
            result = terminate_reason_ids.ids
        return result

    @api.model
    def create(self, vals):
        _super = super(BaseTerminateReasonConfigurator, self)
        res = _super.create(vals)

        terminate_reason_ids = self._get_default_reason_ids()
        if terminate_reason_ids:
            res.write({"terminate_reason_ids": [(6, 0, terminate_reason_ids)]})

        return res
