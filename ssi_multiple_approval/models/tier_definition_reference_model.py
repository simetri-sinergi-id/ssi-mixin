# Copyright 2018 Eficent Business and IT Consulting Services S.L.
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class TierDefinition(models.Model):
    _name = "tier.definition_reference_model"
    _description = "Tier Definition Reference Model"
    _rec_name = "model_id"

    model_id = fields.Many2one(
        string="Referenced Model",
        comodel_name="ir.model",
        required=False,
        ondelete="set null",
    )
