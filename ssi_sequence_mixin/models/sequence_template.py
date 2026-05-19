# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from datetime import datetime

import pytz

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools.safe_eval import safe_eval, test_python_expr


class SequenceTemplate(models.Model):
    _name = "sequence.template"
    _description = "Sequence Template"
    _order = "sequence, id"

    DEFAULT_PYTHON_CODE = """# Available variables:
#  - env: Odoo Environment on which the action is triggered.
#  - document: record on which the action is triggered; may be void."""

    @api.model
    def _default_company_id(self):
        return self.env.company

    name = fields.Char(
        string="Name",
        required=True,
        copy=True,
        help="Name of the sequence template.",
    )
    model_id = fields.Many2one(
        string="Referenced Model",
        comodel_name="ir.model",
        index=True,
        required=True,
        copy=True,
        ondelete="cascade",
        help="Model that this sequence template applies to.",
    )
    model = fields.Char(
        related="model_id.model",
        index=True,
        store=True,
        help="Technical model name (auto-computed from Referenced Model).",
    )
    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        default=lambda self: self._default_company_id(),
        copy=True,
        help="Company this sequence template belongs to.",
    )
    sequence = fields.Integer(
        default=5,
        required=True,
        copy=True,
        help="Priority order of this template; lower number = higher priority.",
    )
    initial_string = fields.Char(
        string="Initial String",
        required=True,
        default="/",
        help="Placeholder value used before the sequence number is generated.",
    )
    sequence_field_id = fields.Many2one(
        string="Sequence Field",
        comodel_name="ir.model.fields",
        ondelete="cascade",
        required=True,
        domain="[('model_id', '=', model_id),('ttype','=','char')]",
        help="Char field on the target model where the generated sequence will be stored.",
    )
    date_field_id = fields.Many2one(
        string="Date Field",
        comodel_name="ir.model.fields",
        ondelete="cascade",
        required=True,
        domain="[('model_id', '=', model_id),('ttype','in',['date','datetime'])]",
        help="Date or datetime field used to compute the sequence period.",
    )
    state = fields.Selection(
        string="States",
        selection=[
            ("draft", "Draft"),
            ("apply", "Sequence Applied"),
        ],
        default="draft",
        help="Current state of the sequence template.",
    )
    computation_method = fields.Selection(
        string="Computation Method",
        selection=[
            ("use_domain", "Domain"),
            ("use_python", "Python Code"),
        ],
        default="use_python",
        required=True,
        copy=True,
        help="Method used to determine whether this template applies to a document.",
    )
    domain = fields.Char(
        string="Domain",
        copy=True,
        help="Domain filter to determine if this template applies to the document.",
    )
    python_code = fields.Text(
        string="Python Code",
        default=DEFAULT_PYTHON_CODE
        + "\n#  - result: Return result, the value is boolean."
        + "\nresult = True",
        copy=True,
    )
    sequence_selection_method = fields.Selection(
        string="Sequence Method",
        selection=[
            ("use_sequence", "Sequence"),
            ("use_python", "Python Code"),
        ],
        default="use_python",
        required=True,
        copy=True,
        help="Method used to select the ir.sequence to use for numbering.",
    )
    sequence_id = fields.Many2one(
        string="Sequence",
        comodel_name="ir.sequence",
        help="The ir.sequence used when sequence selection method is 'Sequence'.",
    )
    sequence_python_code = fields.Text(
        string="Python Code",
        default=DEFAULT_PYTHON_CODE
        + "\n#  - sequence: Return sequence, the value is recordset of sequence.",
        copy=True,
    )
    add_custom_prefix = fields.Boolean(
        string="Add Custom Prefix",
        default=False,
        help="When enabled, a custom prefix is prepended to the generated sequence number.",
    )
    prefix_python_code = fields.Text(
        string="Python Code",
        default=DEFAULT_PYTHON_CODE
        + "\n#  - result: Return prefix, the value is string.",
        copy=True,
    )
    add_custom_suffix = fields.Boolean(
        string="Add Custom Suffix",
        default=False,
        help="When enabled, a custom suffix is appended to the generated sequence number.",
    )
    suffix_python_code = fields.Text(
        string="Python Code",
        default=DEFAULT_PYTHON_CODE
        + "\n#  - result: Return suffix, the value is string.",
        copy=True,
    )
    active = fields.Boolean(
        default=True,
        copy=True,
        help="Inactive templates are excluded from sequence generation.",
    )
    note = fields.Text(
        string="Note",
        copy=True,
        help="Additional notes or remarks about this sequence template.",
    )

    @api.onchange(
        "model_id",
    )
    def onchange_sequence_field_id(self):
        self.sequence_field_id = False

    @api.onchange(
        "model_id",
    )
    def onchange_date_field_id(self):
        self.date_field_id = False

    def create_sequence(self, document):
        self.ensure_one()
        result = False
        sequence_date = False
        sequence = self._evaluate_sequence(document)
        if sequence:
            if self.date_field_id:
                sequence_date = getattr(document, self.date_field_id.name)
            if sequence_date:
                result = sequence.next_by_id(sequence_date=sequence_date)
            else:
                result = sequence.next_by_id()

            if self.add_custom_prefix:
                prefix = self._get_prefix_computation(document, sequence_date)
                result = prefix + result
            if self.add_custom_suffix:
                suffix = self._get_suffix_computation(document, sequence_date)
                result = result + suffix

        return result

    def _get_localdict(self, document):
        self.ensure_one()
        return {
            "env": self.env,
            "document": document,
        }

    def _evaluate_sequence(self, document):
        self.ensure_one()
        if not document:
            return False
        try:
            method_name = "_evaluate_sequence_" + self.sequence_selection_method
            result = getattr(self, method_name)(document)
        except Exception as error:
            msg_err = _("Error evaluating conditions.\n %(error)s") % {"error": error}
            raise UserError(msg_err) from error
        return result

    def _evaluate_sequence_use_python(self, document):
        self.ensure_one()
        res = False
        localdict = self._get_localdict(document)
        try:
            safe_eval(self.sequence_python_code, localdict, mode="exec", nocopy=True)
            res = localdict["sequence"]
        except Exception as error:
            raise UserError(
                _("Error evaluating conditions.\n %(error)s") % {"error": error}
            ) from error
        return res

    def _evaluate_sequence_use_sequence(self, document):
        self.ensure_one()
        result = False
        if self.sequence_id:
            result = self.sequence_id
        return result

    def _get_prefix(self, document):
        self.ensure_one()
        res = False
        localdict = self._get_localdict(document)
        try:
            safe_eval(self.prefix_python_code, localdict, mode="exec", nocopy=True)
            res = localdict["result"]
        except Exception as error:
            raise UserError(
                _("Error on get prefix.\n %(error)s") % {"error": error}
            ) from error
        return res

    def _get_suffix(self, document):
        self.ensure_one()
        result = False
        localdict = self._get_localdict(document)
        try:
            safe_eval(self.suffix_python_code, localdict, mode="exec", nocopy=True)
            result = localdict["result"]
        except Exception as error:
            raise UserError(
                _("Error on get suffix.\n %(error)s") % {"error": error}
            ) from error
        return result

    def _interpolate(self, s, d):
        return (s % d) if s else ""

    def _interpolation_dict(self, date=None, date_range=None):
        self.ensure_one()
        now = range_date = effective_date = datetime.now(
            pytz.timezone(self._context.get("tz") or "UTC")
        )
        if date or self._context.get("ir_sequence_date"):
            effective_date = fields.Datetime.from_string(
                date or self._context.get("ir_sequence_date")
            )
        if date_range or self._context.get("ir_sequence_date_range"):
            range_date = fields.Datetime.from_string(
                date_range or self._context.get("ir_sequence_date_range")
            )

        sequences = {
            "year": "%Y",
            "month": "%m",
            "day": "%d",
            "y": "%y",
            "doy": "%j",
            "woy": "%W",
            "weekday": "%w",
            "h24": "%H",
            "h12": "%I",
            "min": "%M",
            "sec": "%S",
        }
        res = {}
        for key, format_pattern in sequences.items():
            res[key] = effective_date.strftime(format_pattern)
            res["range_" + key] = range_date.strftime(format_pattern)
            res["current_" + key] = now.strftime(format_pattern)

        return res

    def _get_prefix_computation(self, document, date):
        self.ensure_one()
        result = False
        prefix = self._get_prefix(document)

        d = self._interpolation_dict(date_range=date)

        try:
            interpolated_prefix = self._interpolate(prefix, d)
        except Exception as error:
            raise UserError(
                _("Error on convert prefix.\n %(error)s") % {"error": error}
            ) from error

        result = interpolated_prefix
        return result

    def _get_suffix_computation(self, document, date):
        self.ensure_one()
        result = False
        suffix = self._get_suffix(document)

        d = self._interpolation_dict(date_range=date)

        try:
            interpolated_suffix = self._interpolate(suffix, d)
        except Exception as error:
            raise UserError(
                _("Error on convert suffix.\n %(error)s") % {"error": error}
            ) from error

        result = interpolated_suffix
        return result

    # @api.model_cr
    def _register_hook(self):
        return True

    @api.constrains(
        "python_code",
    )
    def _check_python_code(self):
        for action in self.sudo().filtered("python_code"):
            msg = test_python_expr(expr=action.python_code.strip(), mode="exec")
            if msg:
                msg1 = "Template:\n"
                raise ValidationError(msg1 + msg)

    @api.constrains(
        "sequence_python_code",
    )
    def _check_sequence_python_code(self):
        for action in self.sudo().filtered("sequence_python_code"):
            msg = test_python_expr(
                expr=action.sequence_python_code.strip(), mode="exec"
            )
            if msg:
                msg1 = "Sequence:\n"
                raise ValidationError(msg1 + msg)

    @api.constrains(
        "prefix_python_code",
    )
    def _check_prefix_python_code(self):
        for action in self.sudo().filtered("prefix_python_code"):
            msg = test_python_expr(expr=action.prefix_python_code.strip(), mode="exec")
            if msg:
                msg1 = "Prefix:\n"
                raise ValidationError(msg1 + msg)

    @api.constrains(
        "suffix_python_code",
    )
    def _check_suffix_python_code(self):
        for action in self.sudo().filtered("suffix_python_code"):
            msg = test_python_expr(expr=action.suffix_python_code.strip(), mode="exec")
            if msg:
                msg1 = "Suffix:\n"
                raise ValidationError(msg1 + msg)
