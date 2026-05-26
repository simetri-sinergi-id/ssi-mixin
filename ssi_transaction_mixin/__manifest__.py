# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0.html).
{
    "name": "Transaction Mixin",
    "version": "18.0.1.0.0",
    "website": "https://github.com/simetri-sinergi-id/ssi-mixin",
    "author": "PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "mail",
        "ssi_policy_mixin",
        "ssi_sequence_mixin",
        "ssi_decorator",
        "ssi_print_mixin",
    ],
    "data": [
        "menu.xml",
        "views/mixin_transaction_views.xml",
    ],
}
