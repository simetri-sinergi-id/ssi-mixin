# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class TestTransactionDetailMixin(models.Model):
    _name = "test.transaction_detail_mixin"
    _description = "Test Transaction Detail Mixin"
    _inherit = [
        "mixin.product_line_price",
    ]

    test_transaction_id = fields.Many2one(
        string="# Transaction",
        comodel_name="test.transaction_mixin",
        required=True,
        ondelete="cascade",
        help="Referensi ke dokumen transaksi induk.",
    )
