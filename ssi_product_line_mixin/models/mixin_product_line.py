# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class MixinProductLine(models.AbstractModel):
    """
    Abstract mixin for product-line child records (detail rows) in a
    transactional document.

    Provides ``product_id``, ``name`` (description), ``uom_quantity``,
    ``uom_id``, and a computed ``quantity`` (converted to the product’s base
    UoM). Onchange handlers auto-fill the description and UoM from the
    selected product. The ``_field_for_name`` attribute controls which product
    field populates ``name``.
    """

    _name = "mixin.product_line"
    _description = "Product Line Mixin"
    _field_for_name = "display_name"

    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=5,
        help="Order of this line within the document.",
    )
    product_id = fields.Many2one(
        string="Product",
        comodel_name="product.product",
        help="Product for this line.",
    )
    product_category_id = fields.Many2one(
        string="Product Category",
        related="product_id.categ_id",
        store=True,
        help="Category of the selected product.",
    )
    name = fields.Char(
        string="Description",
        required=True,
        help="Line description, auto-filled from the product's display name.",
    )
    uom_quantity = fields.Float(
        string="UoM Quantity",
        required=True,
        default=1.0,
        help="Quantity expressed in the selected unit of measure.",
    )

    @api.depends("product_id")
    def _compute_allowed_uom_ids(self):
        UoM = self.env["uom.uom"]
        for record in self:
            result = []
            if record.product_id:
                criteria = [
                    ("category_id", "=", record.product_id.uom_id.id),
                ]
                result = UoM.search(criteria).ids
            record.allowed_uom_ids = result

    allowed_uom_ids = fields.Many2many(
        string="Allowed UoMs",
        comodel_name="uom.uom",
        compute="_compute_allowed_uom_ids",
        compute_sudo=True,
        help="Units of measure available for selection, "
        "filtered by the product's UoM category.",
    )
    uom_id = fields.Many2one(
        string="UoM",
        comodel_name="uom.uom",
        help="Unit of measure for this line. "
        "Must belong to the same category as the product's UoM.",
    )

    @api.depends(
        "uom_id",
        "product_id",
        "uom_quantity",
    )
    def _compute_qty(self):
        for record in self:
            result = record.uom_quantity
            if record.uom_id and record.product_id:
                product_uom_id = record.product_id.uom_id
                result = record.uom_id._compute_quantity(
                    record.uom_quantity, product_uom_id
                )
            record.quantity = result

    quantity = fields.Float(
        string="Quantity",
        required=False,
        compute="_compute_qty",
        store=True,
        help="Quantity converted to the product's base unit of measure.",
    )
    note = fields.Text(
        string="Note",
        help="Free-text remark for this line.",
    )

    @api.onchange(
        "product_id",
    )
    def onchange_name(self):
        self.name = False
        if self.product_id:
            self.name = getattr(self.product_id, self._field_for_name)

    @api.onchange(
        "product_id",
    )
    def onchange_uom_id(self):
        self.uom_id = False
        if self.product_id:
            self.uom_id = self.product_id.uom_id

    @api.onchange(
        "product_id",
    )
    def onchange_sequence(self):
        self.sequence = 0
        if self.product_id:
            self.sequence = self.product_id.sequence
