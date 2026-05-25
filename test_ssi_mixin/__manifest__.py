# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0.html).
{
    "name": "Test Module: SSI Mixin",
    "version": "18.0.1.0.0",
    "website": "https://github.com/open-synergy/ssi-mixin",
    "author": "PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_master_data_mixin",
    ],
    "data": [
        "security/res_groups/test_mixin_type.xml",
        "security/ir_model_access/test_mixin_type.xml",
        "menu.xml",
        "views/test_mixin_type.xml",
    ],
}
