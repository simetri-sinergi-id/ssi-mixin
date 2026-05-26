# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).
from odoo.tests.common import tagged

from .base import BaseCase


@tagged("post_install", "-at_install")
class TestTransactionMixin(BaseCase):
    def test_create_default_values(self):
        """Record baru dibuat dengan name='/' dan state='draft' secara default."""
        doc = self.test_model.with_user(self.test_user_1.id).create({})
        self.assertEqual(doc.name, "/")
        self.assertEqual(doc.state, "draft")
        self.assertEqual(doc.user_id, self.test_user_1)

    def test_name_get_slash_uses_star_id(self):
        """name_get mengembalikan '*{id}' ketika name masih '/'."""
        doc = self.test_model.with_user(self.test_user_1.id).create({})
        result = doc.name_get()
        self.assertEqual(result, [(doc.id, f"*{doc.id}")])

    def test_name_get_manual_number_uses_name(self):
        """name_get mengembalikan nilai name ketika name bukan '/'."""
        doc = self.test_model.with_context(bypass_policy_check=True).create(
            {"name": "TXN/2026/0001"}
        )
        result = doc.name_get()
        self.assertEqual(result, [(doc.id, "TXN/2026/0001")])

    def test_display_name_computed_from_name(self):
        """display_name dihitung dari name_get — sync dengan name."""
        doc = self.test_model.with_context(bypass_policy_check=True).create(
            {"name": "TXN/2026/0002"}
        )
        self.assertEqual(doc.display_name, "TXN/2026/0002")

    def test_display_name_slash_shows_star_id(self):
        """display_name menampilkan '*{id}' ketika name adalah '/'."""
        doc = self.test_model.with_user(self.test_user_1.id).create({})
        self.assertEqual(doc.display_name, f"*{doc.id}")

    def test_unlink_draft_slash_name_allowed(self):
        """Dokumen draft dengan name='/' dapat dihapus."""
        doc = self.test_model.with_user(self.test_user_1.id).create({})
        doc_id = doc.id
        doc.unlink()
        self.assertFalse(self.test_model.search([("id", "=", doc_id)]).exists())

    def test_action_restart_resets_state_to_draft(self):
        """action_restart mengubah state kembali ke 'draft'."""
        doc = self.test_model.with_user(self.test_user_1.id).create({})
        # Set ke confirmed langsung (bypass normal flow)
        doc.write({"state": "confirmed"})
        self.assertEqual(doc.state, "confirmed")
        # Jalankan restart dengan bypass policy
        doc.with_context(bypass_policy_check=True).action_restart()
        self.assertEqual(doc.state, "draft")

    def test_action_reset_document_number_resets_to_slash(self):
        """action_reset_document_number mengubah name kembali ke '/'."""
        doc = self.test_model.with_context(bypass_policy_check=True).create(
            {"name": "TXN/2026/0003"}
        )
        self.assertEqual(doc.name, "TXN/2026/0003")
        doc.with_context(bypass_policy_check=True).action_reset_document_number()
        self.assertEqual(doc.name, "/")
