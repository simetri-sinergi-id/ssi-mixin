# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "QR Code Mixin",
    "version": "15.0.1.0.0",
    "website": "https://github.com/simetri-sinergi-id/ssi-mixin",
    "author": "PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_decorator",
    ],
    "external_dependencies": {
        "python": [
            "qrcode",
        ],
    },
    "data": [
        "templates/mixin_qr_code_templates.xml",
        "views/ir_model_views.xml",
    ],
}
