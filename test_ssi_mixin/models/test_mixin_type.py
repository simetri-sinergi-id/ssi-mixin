# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0.html).

from odoo import fields, models


class TestMixinType(models.Model):
    _name = "test.mixin.type"
    _inherit = ["mixin.master_data"]
    _description = "Test Mixin Type"

    value = fields.Integer(
        string="Value",
    )
