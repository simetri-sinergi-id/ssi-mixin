# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Mixin Class for Terminate State",
    "version": "14.0.1.0.0",
    "category": "Tools",
    "website": "https://github.com/OCA/ssi-mixin",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/base_terminate_reason_common_data.xml",
        "views/base_terminate_reason.xml",
        "views/base_terminate_reason_configurator.xml",
        "wizards/base_terminate_reason_wizard.xml",
    ],
}
