# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).
from ddt import ddt, file_data

from odoo.tests.common import tagged

from .base import BaseCase


@tagged("post_install", "-at_install")
@ddt
class TestCreate(BaseCase):
    @file_data("scenario_create_invalid_data.yml")
    def test_create_invalid_data_raises(self, data):
        # value="-" on Integer field raises ValueError at Python level (before DB)
        with self.assertRaises(ValueError):
            self.test_model.with_user(self.test_user_1.id).create(
                {
                    "name": data.get("name"),
                    "code": data.get("code"),
                    "value": data.get("value"),
                    "note": data.get("note"),
                }
            )
