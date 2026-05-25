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
        # required=True violated via create() raises DB exception, not ValidationError
        with self.assertRaises(Exception):  # noqa: B017
            self.test_model.with_user(self.test_user_1.id).create(
                {
                    "name": data.get("name"),
                    "code": data.get("code"),
                    "value": data.get("value"),
                    "note": data.get("note"),
                }
            )
