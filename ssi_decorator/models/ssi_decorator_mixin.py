# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from inspect import getmembers

from lxml import etree, html

from odoo import api, models


class MixinDecorator(models.AbstractModel):
    _name = "mixin.decorator"
    _description = "SSI Decorator Mixin"

    @api.model
    def fields_view_get(
        self, view_id=None, view_type="form", toolbar=False, submenu=False
    ):
        """
        Override to allow decorator-based view element injection.
        This enables dynamic injection of elements into form, search, or tree views
        using decorator patterns defined in the class.
        """
        result = super().fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu
        )
        View = self.env["ir.ui.view"]

        view_arch = etree.XML(result["arch"])

        if view_type == "form":
            view_arch = self._run_insert_on_form_view(view_arch)
        elif view_type == "search":
            view_arch = self._run_insert_on_search_view(view_arch)
        elif view_type == "tree":
            view_arch = self._run_insert_on_tree_view(view_arch)

        if view_id and result.get("base_model", self._name) != self._name:
            View = View.with_context(base_model_name=result["base_model"])
        new_arch, new_fields = View.postprocess_and_fields(view_arch, self._name)
        result["arch"] = new_arch
        new_fields.update(result["fields"])
        result["fields"] = new_fields

        return result

    @api.model
    def _run_insert_on_tree_view(self, view_arch):
        """
        Run all methods decorated for tree view injection.
        """
        cls = type(self)
        methods = []
        for _attr, func in getmembers(cls):
            if self.is_api_model_decorator(func, "_insert_on_tree_view"):
                methods.append(func)
        if methods:
            view_arch = self.run_decorator_field_view_get_method(methods, view_arch)
        return view_arch

    @api.model
    def _run_insert_on_search_view(self, view_arch):
        """
        Run all methods decorated for search view injection.
        """
        cls = type(self)
        methods = []
        for _attr, func in getmembers(cls):
            if self.is_api_model_decorator(func, "_insert_on_search_view"):
                methods.append(func)
        if methods:
            view_arch = self.run_decorator_field_view_get_method(methods, view_arch)
        return view_arch

    @api.model
    def _run_insert_on_form_view(self, view_arch):
        """
        Run all methods decorated for form view injection.
        """
        cls = type(self)
        methods = []
        for _attr, func in getmembers(cls):
            if self.is_api_model_decorator(func, "_insert_on_form_view"):
                methods.append(func)
        if methods:
            view_arch = self.run_decorator_field_view_get_method(methods, view_arch)
        return view_arch

    def is_decorator(self, func, decorator):
        """
        Check if a function is decorated with a specific decorator attribute.
        """
        self.ensure_one()
        return callable(func) and hasattr(func, decorator)

    def run_decorator_method(self, methods):
        """
        Run all decorator methods (for business logic hooks).
        """
        self.ensure_one()
        for method_name in methods:
            getattr(self, method_name.__name__)()

    def is_api_model_decorator(self, func, decorator):
        """
        Check if a function is decorated for API model view injection.
        """
        return callable(func) and hasattr(func, decorator)

    def run_decorator_field_view_get_method(self, methods, view_arch):
        """
        Run all decorator methods for view field injection.
        """
        for method_name in methods:
            view_arch = getattr(self, method_name.__name__)(view_arch)
        return view_arch

    @api.model
    def _add_view_element(
        self, view_arch, qweb_template_xml_id, xpath, position="after", order=False
    ):
        """
        Add a rendered QWeb template element to a view at a given xpath.
        Handles position (after, before, inside) and order for insertion.
        """
        additional_element = self.env["ir.qweb"]._render(qweb_template_xml_id)
        if len(view_arch.xpath(xpath)) == 0:
            return view_arch
        node_xpath = view_arch.xpath(xpath)[0]
        for frag in html.fragments_fromstring(additional_element):
            if order:
                frag.set("order", str(order))
            if position == "after":
                node_xpath.addnext(frag)
            elif position == "before":
                node_xpath.addprevious(frag)
            elif position == "inside":
                node_xpath.insert(0, frag)
        return view_arch
