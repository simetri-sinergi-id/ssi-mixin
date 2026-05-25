# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Test Module: Policy Mixin",
    "version": "14.0.1.2.0",
    "category": "Administration",
    "website": "https://github.com/open-synergy/ssi-mixin",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": False,
    "depends": [
        "mail",
        "ssi_policy_mixin",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/policy_template_data.xml",
        "views/test_policy_type_view.xml",
        "views/test_policy_view.xml",
    ],
}
