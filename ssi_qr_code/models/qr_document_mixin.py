# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging
from base64 import b64encode

from cStringIO import StringIO

from odoo import api, fields, models

_logger = logging.getLogger(__name__)

try:
    from qrcode import QRCode, constants as qr_constants
except (ImportError, IOError) as err:
    _logger.debug(err)


class QrDocumentMixin(models.AbstractModel):
    _name = "qr.document.mixin"
    _description = "QR Document"

    def _compute_qr_image(self):
        for document in self:
            qrcode_content = document._get_qrcode_content()
            qr = QRCode(
                version=1,
                error_correction=qr_constants.ERROR_CORRECT_L,
                box_size=5,
                border=4,
            )
            qr.add_data(qrcode_content)
            qr.make(fit=True)
            qr_image = qr.make_image()
            temp_file = StringIO()
            qr_image.save(temp_file)
            qr_image = b64encode(temp_file.getvalue())
            document.qr_image = qr_image

    qr_image = fields.Binary(
        string="QR Code",
        compute="_compute_qr_image",
        store=False,
    )

    def _get_qrcode_content(self):
        self.ensure_one()
        criteria = [
            ("name.model", "=", self._name),
        ]
        obj_content = self.env["base.qr_content_policy"]
        content_policy = obj_content.search(criteria)
        if len(content_policy) > 0:
            content = content_policy[0]._get_content(self)
        else:
            content = self._get_standard_content()
        return content

    def _get_standard_content(self):
        self.ensure_one()
        odoo_url = self.env["ir.config_parameter"].get_param("web.base.url")
        document_url = "/web?#id=%d&view_type=form&model=%s" % (
            self.id,
            self._name,
        )
        full_url = odoo_url + document_url
        return full_url
