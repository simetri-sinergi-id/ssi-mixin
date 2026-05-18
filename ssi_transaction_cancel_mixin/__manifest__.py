# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Transaction Mixin - Cancel State",
    "version": "15.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_transaction_mixin",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizards/base_select_cancel_reason_views.xml",
        "templates/mixin_transaction_cancel_templates.xml",
        "views/ir_model_views.xml",
        "views/base_cancel_reason_views.xml",
    ],
    "demo": [
        "demo/base_cancel_reason_demo.xml",
    ],
}
