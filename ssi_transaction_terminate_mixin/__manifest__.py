# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Transaction Mixin - Terminate State",
    "version": "15.0.1.1.0",
    "website": "https://github.com/simetri-sinergi-id/ssi-mixin",
    "author": "PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_transaction_mixin",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizards/base_select_terminate_reason_views.xml",
        "templates/mixin_transaction_terminate_templates.xml",
        "views/ir_model_views.xml",
        "views/base_terminate_reason_views.xml",
    ],
    "demo": [
        "demo/base_terminate_reason_demo.xml",
    ],
}
