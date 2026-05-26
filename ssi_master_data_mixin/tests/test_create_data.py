# Copyright YYYY OpenSynergy Indonesia
# Copyright YYYY PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).
from odoo.tests.common import tagged

from .base import BaseCase


@tagged("post_install", "-at_install")
class TestCreate(BaseCase):
    def test_create_valid_data(self):
        """Membuat master data dengan data valid."""
        self.run_yaml_scenario("scenario_create_data.yaml")
