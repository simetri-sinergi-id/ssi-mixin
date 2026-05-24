# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MixinTaxLine(models.AbstractModel):
    """
    Abstract child-record model representing a single tax line within a
    transactional document.

    Inherits ``mixin.account_move_single_line`` and pre-configures the field
    name pointers so the tax amount is posted to the designated tax account.
    Concrete implementations attach this as a ``One2many`` child on the parent
    transactional model.
    """

    _name = "mixin.tax_line"
    _description = "Tax Line Mixin"
    _inherit = [
        "mixin.account_move_single_line",
    ]

    _analytic_account_id_field_name = "analytic_account_id"
    _label_field_name = "name"
    _amount_currency_field_name = "tax_amount"

    name = fields.Char(
        string="Description",
        required=True,
        help="Short description of this tax line.",
    )
    tax_id = fields.Many2one(
        string="Tax",
        comodel_name="account.tax",
        required=True,
        help="Tax applied on this line.",
    )
    account_id = fields.Many2one(
        string="Account",
        comodel_name="account.account",
        required=True,
        help="General ledger account used to post the tax amount.",
    )
    analytic_account_id = fields.Many2one(
        string="Analytic Account",
        comodel_name="account.analytic.account",
        help="Analytic account for cost/revenue allocation of this tax line.",
    )
    currency_id = fields.Many2one(
        string="Currency",
        comodel_name="res.currency",
        help="Currency used for this tax line.",
    )
    base_amount = fields.Monetary(
        string="Base Amount",
        currency_field="currency_id",
        required=True,
        help="Taxable base amount for this tax line.",
    )
    tax_amount = fields.Monetary(
        string="Tax Amount",
        currency_field="currency_id",
        required=True,
        help="Computed tax amount for this tax line.",
    )
    manual = fields.Boolean(
        string="Manual",
        default=True,
        help="When checked, this tax line is entered manually "
        "and not recomputed automatically.",
    )
    move_line_id = fields.Many2one(
        string="Journal Item",
        comodel_name="account.move.line",
        readonly=True,
        copy=False,
        help="Journal item generated when this tax line is posted.",
    )
