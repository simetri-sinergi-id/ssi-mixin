# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models

from odoo.addons.ssi_decorator import ssi_decorator


class MixinResCurrencyM2OConfigurator(models.AbstractModel):
    """
    Mixin that adds configurable filtering for ``res.currency`` Many2one
    fields using the three-strategy pattern from ``mixin.many2one_configurator``
    (manual, domain, or Python code).

    Inherits ``mixin.decorator`` and optionally injects the configuration
    widget into the form view when
    ``_res_currency_m2o_configurator_insert_form_element_ok`` is ``True``.
    """

    _name = "mixin.res_currency_m2o_configurator"
    _inherit = [
        "mixin.decorator",
    ]
    _description = "res.currency Many2one Configurator Mixin"

    _res_currency_m2o_configurator_insert_form_element_ok = False
    _res_currency_m2o_configurator_form_xpath = False

    currency_selection_method = fields.Selection(
        default="domain",
        selection=[("manual", "Manual"), ("domain", "Domain"), ("code", "Python Code")],
        string="Currency Selection Method",
        required=True,
        help="Method used to filter available currencies: manual selection, "
        "domain expression, or Python code.",
    )
    currency_ids = fields.Many2many(
        comodel_name="res.currency",
        string="Currencies",
        help="Manually selected currencies available for selection (used when "
        "Currency Selection Method is 'Manual').",
    )
    currency_domain = fields.Text(
        default="[]",
        string="Currency Domain",
        help="Domain expression to filter available currencies (used when "
        "Currency Selection Method is 'Domain').",
    )
    currency_python_code = fields.Text(
        default="result = []",
        string="Currency Python Code",
        help="Python code evaluated to produce the list of available currencies. "
        "Must assign a recordset to 'result' "
        "(used when Currency Selection Method is 'Python Code').",
    )

    @ssi_decorator.insert_on_form_view()
    def _res_currency_m2o_configurator_insert_form_element(self, view_arch):
        # TODO
        template_xml = "ssi_res_currency_m2o_configurator_mixin."
        template_xml += "res_currency_m2o_configurator_template"
        if self._res_currency_m2o_configurator_insert_form_element_ok:
            view_arch = self._add_view_element(
                view_arch=view_arch,
                qweb_template_xml_id=template_xml,
                xpath=self._res_currency_m2o_configurator_form_xpath,
                position="inside",
            )
        return view_arch
