# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Master Data Mixin",
    "version": "15.0.1.0.0",
    "website": "https://github.com/simetri-sinergi-id",
    "author": "PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "mail",
        "ssi_print_mixin",
        "ssi_sequence_mixin",
    ],
    "data": [
        "views/mixin_master_data_views.xml",
    ],
}
