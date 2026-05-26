# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).
from odoo.exceptions import UserError
from odoo.tests.common import tagged

from .base import BaseCase


@tagged("post_install", "-at_install")
class TestTransactionMixinErrors(BaseCase):
    def test_unlink_non_draft_raises_user_error(self):
        """unlink gagal dengan UserError jika state bukan 'draft'."""
        doc = self.test_model.with_user(self.test_user_1.id).create({})
        doc.write({"state": "confirmed"})
        with self.assertRaises(UserError):
            doc.unlink()

    def test_unlink_manual_number_raises_user_error(self):
        """unlink gagal dengan UserError jika name bukan '/'."""
        doc = self.test_model.with_context(bypass_policy_check=True).create(
            {"name": "TXN/2026/MANUAL"}
        )
        with self.assertRaises(UserError):
            doc.unlink()

    def test_duplicate_document_number_raises_user_error(self):
        """Membuat dua dokumen dengan name yang sama (bukan '/') memicu UserError."""
        self.test_model.with_context(bypass_policy_check=True).create(
            {"name": "TXN/2026/DUP"}
        )
        with self.assertRaises(UserError):
            self.test_model.with_context(bypass_policy_check=True).create(
                {"name": "TXN/2026/DUP"}
            )

    def test_restart_without_policy_raises_user_error(self):
        """action_restart memunculkan UserError jika restart_ok=False
        dan tidak ada bypass."""
        doc = self.test_model.with_user(self.test_user_1.id).create({})
        doc.write({"state": "confirmed"})
        # Tanpa bypass dan tanpa policy template → restart_ok=False
        with self.assertRaises(UserError):
            doc.action_restart()

    def test_reset_document_number_without_policy_raises_user_error(self):
        """action_reset_document_number memunculkan UserError
        jika manual_number_ok=False."""
        doc = self.test_model.with_context(bypass_policy_check=True).create(
            {"name": "TXN/2026/NOPOLICY"}
        )
        # Hapus bypass — tanpa policy template → manual_number_ok=False
        with self.assertRaises(UserError):
            doc.action_reset_document_number()
