# Copyright 2019 ForgeFlow S.L. (https://www.forgeflow.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, modules


class Users(models.Model):
    _inherit = "res.users"

    review_ids = fields.Many2many(string="Reviews", comodel_name="tier.review")

    @api.model
    def review_user_count(self):
        user_reviews = {}
        to_review_docs = {}
        reviews = self.env["tier.review"].search(
            [
                ("status", "=", "pending"),
                ("id", "in", self.env.user.review_ids.ids),
            ]
        )
        for review in reviews:
            record = (
                review.env[review.model]
                .with_user(self.env.user)
                .search([("id", "=", review.res_id)])
            )
            if not record or record.rejected:
                # Checking that the review is accessible with the permissions
                # and to review condition is valid
                continue
            if not user_reviews.get(review["model"]):
                user_reviews[review.model] = {
                    "name": record._description,
                    "model": review.model,
                    "icon": modules.module.get_module_icon(
                        self.env[review.model]._original_module
                    ),
                    "pending_count": 0,
                }
            docs = to_review_docs.get(review.model)
            if (docs and record not in docs) or not docs:
                user_reviews[review.model]["pending_count"] += 1
            to_review_docs.setdefault(review.model, []).append(record)
        return list(user_reviews.values())

    @api.model
    def get_reviews(self, data):
        review_obj = self.env["tier.review"].with_context(lang=self.env.user.lang)
        res = review_obj.search_read([("id", "in", data.get("res_ids"))])
        for r in res:
            # Get the translated status value.
            r["display_status"] = dict(
                review_obj.fields_get("status")["status"]["selection"]
            ).get(r.get("status"))
            # Convert to datetime timezone
            # if r["reviewed_date"]:
            #     r["reviewed_date"] = fields.Datetime.context_timestamp(
            #         self, r["reviewed_date"]
            #     )
        return res
