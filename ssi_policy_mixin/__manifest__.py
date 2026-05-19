# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Policy Mixin",
    "version": "15.0.1.0.0",
    "category": "Administration",
    "website": "https://github.com/simetri-sinergi-id/ssi-mixin",
    "author": "PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        "security/ir.model.access.csv",
        "menu.xml",
        "views/policy_template_views.xml",
        "views/policy_template_detail_views.xml",
    ],
}
