# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).
from odoo.tests.common import tagged

from .base import BaseCase


@tagged("post_install", "-at_install")
class TestSequenceGeneration(BaseCase):
    def test_python_computation_method(self):
        """Sequence dihasilkan ketika python_code mengembalikan True."""
        self.run_yaml_scenario("scenario_python_method.yaml")

    def test_domain_computation_method(self):
        """Sequence dihasilkan ketika domain filter cocok dengan dokumen."""
        self.run_yaml_scenario("scenario_domain_method.yaml")

    def test_initial_string_skip_sequence(self):
        """Sequence tidak di-generate ulang jika name sudah bukan initial_string."""
        self.run_yaml_scenario("scenario_initial_string_skip.yaml")

    def test_template_order_selection(self):
        """Template dengan nilai sequence tertinggi dipilih terlebih dahulu."""
        self.run_yaml_scenario("scenario_template_order.yaml")

    def test_custom_prefix(self):
        """Prefix custom dari prefix_python_code disisipkan sebelum nomor urut."""
        self.run_yaml_scenario("scenario_custom_prefix.yaml")

    def test_custom_suffix(self):
        """Suffix custom dari suffix_python_code ditambahkan setelah nomor urut."""
        self.run_yaml_scenario("scenario_custom_suffix.yaml")

    def test_prefix_and_suffix_combined(self):
        """Prefix dan suffix custom keduanya diterapkan sekaligus."""
        self.run_yaml_scenario("scenario_prefix_suffix.yaml")
