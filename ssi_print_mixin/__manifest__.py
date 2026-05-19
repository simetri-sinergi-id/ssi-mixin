# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Print Policy Mixin",
    "version": "15.0.1.1.0",
    "website": "https://github.com/simetri-sinergi-id/ssi-mixin",
    "author": "PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "base",
        "mail",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizards/base_print_document.xml",
        "templates/mixin_print_templates.xml",
        "views/print_document_type_views.xml",
        "views/ir_actions_report_views.xml",
    ],
}
