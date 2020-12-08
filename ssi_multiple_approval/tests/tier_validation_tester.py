# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class TierValidationTester(models.Model):
    _name = "tier.validation.tester"
    _description = "Tier Validation Tester"
    _inherit = [
        "tier.validation.mixin",
    ]
    _state_from = ["draft", "confirm"]
    _state_to = [
        "open",
    ]

    name = fields.Char(
        string="# Document",
        required=True,
    )

    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("open", "On Progress"),
            ("done", "Finished"),
            ("cancel", "Cancelled"),
        ],
        default="draft",
    )

    def action_confirm(self):
        for document in self:
            document.write({"state": "confirm"})
            # document.request_validation()

    def action_open(self):
        for document in self:
            document.write({"state": "open"})

    def action_cancel(self):
        for document in self:
            document.write({"state": "cancel"})
            document.restart_validation()

    def validate_tier(self):
        _super = super(TieValidationTester, self)
        _super.validate_tier()
        for document in self:
            if document.validated:
                document.action_open()
