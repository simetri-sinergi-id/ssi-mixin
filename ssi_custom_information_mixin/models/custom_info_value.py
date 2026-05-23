# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import _, api, fields, models
from odoo.tools.misc import get_lang


class CustomInfoValue(models.Model):
    _description = "Custom information value"
    _name = "custom_info.value"
    _rec_name = "value"

    model = fields.Char(
        string="Related Document Model",
        index=True,
        help="Technical name of the model the value is linked to.",
    )
    res_id = fields.Integer(
        string="Related Document ID",
        index=True,
        help="ID of the record the value is linked to.",
    )
    detail_id = fields.Many2one(
        comodel_name="custom_info.template_detail",
        required=True,
        string="Template Detail",
        help="Template detail that defines this value's property.",
    )
    property_id = fields.Many2one(
        comodel_name="custom_info.property",
        related="detail_id.property_id",
        string="Property",
        help="Custom property definition.",
    )
    sequence = fields.Integer(
        string="Sequence",
        index=True,
        readonly=True,
        related="detail_id.sequence",
        store=True,
        help="Display order, inherited from template detail.",
    )
    category_id = fields.Many2one(
        string="Category",
        related="detail_id.category_id",
        store=True,
        readonly=True,
        help="Category, inherited from template detail.",
    )
    name = fields.Char(
        string="Name",
        related="property_id.name",
        readonly=True,
        help="Property name.",
    )
    field_type = fields.Selection(
        string="Field Type",
        related="property_id.field_type",
        readonly=True,
        help="Data type of this property.",
    )

    @api.depends(
        "property_id.field_type",
    )
    def _compute_field_name(self):
        """Get the technical name where the real typed value is stored."""
        for s in self:
            s.field_name = f"value_{s.property_id.field_type!s}"

    field_name = fields.Char(
        compute="_compute_field_name",
        help="Technical name of the field where the value is stored.",
    )

    @api.model
    def _search_value(self, operator, value):
        """Search from the stored field directly."""
        options = (
            o[0]
            for o in self.property_id._fields["field_type"].get_description(self.env)[
                "selection"
            ]
        )
        domain = []
        for fmt in options:
            try:
                _value = (
                    self._transform_value(value, fmt)
                    if not isinstance(value, list)
                    else [self._transform_value(v, fmt) for v in value]
                )
            except ValueError:
                # If you are searching something that cannot be casted, then
                # your property is probably from another type
                continue
            domain += [
                "&",
                ("field_type", "=", fmt),
                ("value_" + fmt, operator, _value),
            ]
        return ["|"] * (len(domain) // 3 - 1) + domain

    @api.depends(
        "property_id.field_type",
        "field_name",
        "value_str",
        "value_int",
        "value_float",
        "value_bool",
        "value_id",
    )
    def _compute_value(self):
        """Get the value as a string, from the original field."""
        for s in self:
            if s.field_type == "id":
                s.value = s.value_id.display_name
            elif s.field_type == "bool":
                s.value = _("Yes") if s.value_bool else _("No")
            elif s.field_type == "date":
                s.value = getattr(s, s.field_name, False)
            elif s.field_type == "datetime":
                s.value = getattr(s, s.field_name, False)
            elif s.field_type == "ids":
                num_ids = 1
                result = ""
                for value in s.value_ids:
                    result += f"{num_ids}) {value.name} \n"
                    num_ids += 1
                s.value = result
            elif s.field_type in ["int", "float"]:
                if s.field_type == "int":
                    fmt = "%.0f"
                else:
                    fmt = "%.2f"
                lang = get_lang(self.env)
                amount = float(getattr(s, s.field_name, False))
                formatted_amount = lang.format(
                    fmt, amount, grouping=True, monetary=True
                )
                s.value = formatted_amount
            else:
                s.value = getattr(s, s.field_name, False)

    value = fields.Char(
        compute="_compute_value",
        help="Value, always converted to/from the typed field.",
    )
    value_str = fields.Char(
        string="Text value",
        translate=True,
        index=True,
        help="Value for text-type properties.",
    )
    value_int = fields.Integer(
        string="Whole number value",
        index=True,
        help="Value for integer-type properties.",
    )
    value_float = fields.Float(
        string="Decimal number value",
        index=True,
        help="Value for decimal-type properties.",
    )
    value_bool = fields.Boolean(
        string="Yes/No value",
        index=True,
        help="Value for boolean-type properties.",
    )
    value_date = fields.Date(
        string="Date value",
        index=True,
        help="Value for date-type properties.",
    )
    value_datetime = fields.Datetime(
        string="Datetime value",
        index=True,
        help="Value for datetime-type properties.",
    )
    value_id = fields.Many2one(
        string="Selection value",
        comodel_name="custom_info.option",
        ondelete="cascade",
        domain="[]",
        help="Value for single-selection properties.",
    )
    value_ids = fields.Many2many(
        string="Multiple Selection value",
        comodel_name="custom_info.option",
        relation="rel_custom_info_value_2_option",
        column1="value_id",
        column2="option_id",
        help="Values for multiple-selection properties.",
    )

    @api.depends(
        "detail_id",
    )
    def _compute_allowed_option_ids(self):
        for record in self:
            result = []
            if record.detail_id and record.detail_id.property_id.field_type in [
                "id",
                "ids",
            ]:
                result = record.detail_id.property_id.option_set_id.option_ids
            record.allowed_option_ids = result

    allowed_option_ids = fields.Many2many(
        string="Allowed Options",
        comodel_name="custom_info.option",
        compute="_compute_allowed_option_ids",
        store=False,
        help="Options allowed for this value, filtered from the property's option set.",
    )
