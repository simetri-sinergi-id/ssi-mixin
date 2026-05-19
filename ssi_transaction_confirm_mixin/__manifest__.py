# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Transaction Mixin - Waiting for Approval State",
    "version": "15.0.1.0.0",
    "website": "https://github.com/simetri-sinergi-id/ssi-mixin",
    "author": "PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_transaction_mixin",
        "ssi_multiple_approval_mixin",
    ],
    "data": [
        "templates/mixin_transaction_confirm_templates.xml",
    ],
}
