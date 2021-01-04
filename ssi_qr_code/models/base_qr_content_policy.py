# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval as eval


class BaseQrContentPolicy(models.Model):
    _name = "base.qr_content_policy"
    _description = "QR Content Policy"

    name = fields.Many2one(
        string="Model",
        comodel_name="ir.model",
        required=True,
    )
    use_standard_content = fields.Boolean(
        string="Use Standard Content",
        default=True,
    )
    python_code = fields.Text(
        string="Python Code for Custom Content",
        default="result = True",
    )
    note = fields.Text(
        string="Note",
    )

    def _get_localdict(self, document):
        self.ensure_one()
        return {
            "env": self.env,
            "document": document,
        }

    def _get_content(self, document):
        self.ensure_one()
        if self.use_standard_content:
            content = document._get_standard_content()
        else:
            content = self._get_custom_content(document)
        return content

    def _get_custom_content(self, document):
        self.ensure_one()
        result = ""
        localdict = self._get_localdict(document)
        try:
            eval(self.python_code, localdict, mode="exec", nocopy=True)
            result = localdict["result"]
        except:  # noqa: E722
            result = ""
        return result
