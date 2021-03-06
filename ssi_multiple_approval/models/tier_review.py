# Copyright 2018 Eficent Business and IT Consulting Services S.L.
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError
from odoo.tools.safe_eval import safe_eval


class TierReview(models.Model):
    _name = "tier.review"
    _description = "Tier Review"

    status = fields.Selection(
        string="Status",
        selection=[
            ("draft", "Draft"),
            ("pending", "Pending"),
            ("rejected", "Rejected"),
            ("approved", "Approved"),
        ],
        default="draft",
    )
    model = fields.Char(
        string="Related Document Model",
        index=True,
    )
    res_id = fields.Integer(
        string="Related Document ID",
        index=True,
    )
    definition_id = fields.Many2one(
        string="Definition",
        comodel_name="tier.definition",
    )
    definition_review_id = fields.Many2one(
        string="Definition Review",
        comodel_name="tier.definition.review",
    )
    review_type = fields.Selection(
        string="Review Type",
        related="definition_review_id.review_type",
        readonly=True,
    )
    reviewer_ids = fields.Many2many(
        string="Reviewers",
        comodel_name="res.users",
        compute="_compute_reviewer_ids",
        store=True,
    )
    reviewer_partner_ids = fields.Many2many(
        string="Review Partners",
        comodel_name="res.partner",
        compute="_compute_reviewer_partner_ids",
    )
    sequence = fields.Integer(
        string="Sequence",
        required=True,
    )
    date = fields.Datetime(
        string="Date",
        readonly=True,
    )
    user_id = fields.Many2one(
        string="Validated/Rejected By",
        comodel_name="res.users",
        readonly=True,
    )

    @api.depends(
        "reviewer_ids",
    )
    def _compute_reviewer_partner_ids(self):
        for rec in self:
            rec.reviewer_partner_ids = rec._get_reviewer_partner_ids()

    def _get_reviewer_partner_ids(self):
        self.ensure_one()
        partner_ids = False
        if self.reviewer_ids:
            partner_ids = self.reviewer_ids.mapped("partner_id")
        return partner_ids

    def _get_object(self):
        document_id = self.res_id
        document_model = self.model

        object = self.env[document_model].browse([document_id])[0]
        return object

    def _get_localdict(self):
        return {
            "rec": self._get_object(),
            "env": self.env,
        }

    def _evaluate_python_code(self, python_condition):
        localdict = self._get_localdict()
        result = False
        try:
            safe_eval(
                python_condition, globals_dict=localdict, mode="exec", nocopy=True
            )
            result = localdict
        except ValueError:
            msg_err = "Error when execute python code"
            raise UserError(_(msg_err))

        return result

    @api.depends(
        "definition_review_id",
    )
    def _compute_reviewer_ids(self):
        for rec in self:
            list_user = []
            if rec.definition_review_id:
                review_type = rec.review_type
                user_ids = rec.definition_review_id.reviewer_ids
                if user_ids:
                    list_user += user_ids.ids

                group_ids = rec.definition_review_id.reviewer_group_ids
                if group_ids:
                    for group in group_ids:
                        list_user += group.users.ids

                if review_type == "python":
                    python_code = rec.definition_review_id.python_code
                    result = rec._evaluate_python_code(python_code)
                    if result:
                        if "user" in result:
                            list_user += result["user"]
                        else:
                            msg_err = "No User defines on python code"
                            raise UserError(_(msg_err))
                rec.reviewer_ids = list(set(list_user))
