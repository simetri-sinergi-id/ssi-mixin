# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Abstract Class for QR Code",
    "version": "14.0.1.0.0",
    "website": "https://github.com/OCA/ssi-mixin",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "base",
    ],
    "external_dependencies": {
        "python": [
            "qrcode",
        ],
    },
    "data": [
        "security/ir.model.access.csv",
        "views/base_qr_content_policy_views.xml",
    ],
}
