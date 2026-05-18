# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class TestSsiMasterData(models.Model):
    _name = "test_ssi_master_data"
    _inherit = ["mixin.master_data"]
    _description = "Test SSI Master Data"
