# Copyright YYYY OpenSynergy Indonesia
# Copyright YYYY PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).
from odoo.tests.common import tagged

from .base import BaseCase


@tagged("post_install", "-at_install")
class TestGenerateCode(BaseCase):
    def test_generate_code(self):
        """Generate code berhasil menggunakan sequence template."""
        self.run_yaml_scenario("scenario_generate_code.yaml")
