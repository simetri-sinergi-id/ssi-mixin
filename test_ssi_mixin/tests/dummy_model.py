# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).
from odoo import fields, models


class DummyTestMixinType(models.Model):
    _name = "ssi.test.mixin.type"
    _inherit = "mixin.master_data"
    _description = "Dummy Test Mixin Type"

    value = fields.Integer(
        string="Input Value",
    )
