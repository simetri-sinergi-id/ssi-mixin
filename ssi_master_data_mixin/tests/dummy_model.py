# Copyright YYYY OpenSynergy Indonesia
# Copyright YYYY PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).
from odoo import fields, models


class DummyTestMasterData(models.Model):
    _name = "ssi.test.master_data_mixin"
    _inherit = "mixin.master_data"
    _description = "Dummy Test Master Data"

    value = fields.Integer(
        string="Input Value",
    )
