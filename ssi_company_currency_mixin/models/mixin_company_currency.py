# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class MixinCompanyCurrency(models.AbstractModel):
    """
    Lightweight mixin that adds a ``company_id`` field and a related,
    stored ``company_currency_id`` field to any model.

    The currency is automatically derived from the selected company so that
    monetary fields on the inheriting model can reference
    ``company_currency_id`` as their ``currency_field``.
    """

    _name = "mixin.company_currency"
    _description = "Company Currency Mixin"

    @api.model
    def _default_company_id(self):
        return self.env.user.company_id.id

    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        required=True,
        default=lambda self: self._default_company_id(),
        copy=True,
        help="Company that owns this record.",
    )
    company_currency_id = fields.Many2one(
        string="Company Currency",
        comodel_name="res.currency",
        related="company_id.currency_id",
        store=True,
        help="Currency of the selected company. "
        "Used as the currency_field for monetary fields on inheriting models.",
    )
