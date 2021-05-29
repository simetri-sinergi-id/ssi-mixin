# Copyright 2018 Eficent Business and IT Consulting Services S.L.
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Multiple Approval",
    "summary": "Implement a validation process based on tiers.",
    "version": "14.0.1.0.0",
    "category": "Tools",
    "website": "https://simetri-sinergi.id",
    "author": "Eficent, Odoo Community Association (OCA), "
    "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "mail",
        "bus",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/tier_definition_view.xml",
        "views/tier_review_view.xml",
        "views/tier_definition_reference_model_view.xml",
        "views/assets_backend.xml",
    ],
    "qweb": [
        "static/src/xml/systray.xml",
        "static/src/xml/tier_review_template.xml",
    ],
}
