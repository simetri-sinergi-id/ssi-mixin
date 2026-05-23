# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Custom Information Mixin",
    "version": "15.0.1.0.0",
    "website": "https://github.com/simetri-sinergi-id/ssi-mixin",
    "author": "PT. Simetri Sinergi Indonesia",
    "category": "Tools",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_decorator",
    ],
    "data": [
        "security/ir.model.access.csv",
        "menu.xml",
        "templates/custom_information_templates.xml",
        "views/custom_info_category_views.xml",
        "views/custom_info_template_views.xml",
        "views/custom_info_option_views.xml",
        "views/custom_info_option_set_views.xml",
        "views/custom_info_value_views.xml",
        "views/custom_info_property_views.xml",
    ],
    "demo": [
        "demo/custom_info_category.xml",
        "demo/custom_info_option.xml",
        "demo/custom_info_option_set.xml",
        "demo/custom_info_property.xml",
    ],
}
