# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ModelConfiguratorTester(models.Model):
    _name = "model.configurator.tester"
    _description = "Model Configurator Tester"
    _inherit = [
        "sequence.configurator.mixin",
    ]

    name = fields.Char(
        string="# Document",
        default="/",
        required=True,
    )
    tester_type_id = fields.Many2one(
        string="Tester Type", comodel_name="model.configurator.tester.type"
    )
    description = fields.Char(
        string="Description",
        required=True,
    )

    @api.model
    def create(self, values):
        _super = super(ModelConfiguratorTester, self)
        result = _super.create(values)
        sequence = result._create_sequence()
        result.write(
            {
                "name": sequence,
            }
        )
        return result


class ModelConfiguratorTesterType(models.Model):
    _name = "model.configurator.tester.type"
    _description = "Model Configurator Tester Type"

    name = fields.Char(
        string="# Document",
        default="/",
        required=True,
    )
    code = fields.Char(
        string="Code",
    )
    sequence_id = fields.Many2one(string="Sequence", comodel_name="ir.sequence")
