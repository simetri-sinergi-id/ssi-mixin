# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo.tests.common import SavepointCase, tagged

from .common import setup_test_model, teardown_test_model
from .tier_validation_tester import TierValidationTester


@tagged("post_install", "-at_install")
class TierValidationTest(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(TierValidationTest, cls).setUpClass()

        setup_test_model(cls.env, [TierValidationTester])

        cls.test_model = cls.env[TierValidationTester._name]

        cls.tester_model = cls.env["ir.model"].search(
            [("model", "=", "tier.validation.tester")]
        )

        # Access record:
        cls.env["ir.model.access"].create(
            {
                "name": "access.tier.validation.tester",
                "model_id": cls.tester_model.id,
                "perm_read": 1,
                "perm_write": 1,
                "perm_create": 1,
                "perm_unlink": 1,
            }
        )

        # Create user.
        cls.user1 = cls.env["res.users"].create(
            {
                "name": "Test User 1",
                "login": "user1",
                "password": "user1",
            }
        )
        cls.user1.partner_id.email = "user1@test.com"

        cls.user2 = cls.env["res.users"].create(
            {
                "name": "Test User 2",
                "login": "user2",
                "password": "user2",
            }
        )
        cls.user2.partner_id.email = "user2@test.com"

        cls.user3 = cls.env["res.users"].create(
            {
                "name": "Test User 3",
                "login": "user3",
                "password": "user3",
            }
        )
        cls.user3.partner_id.email = "user3@test.com"

        # Create Tier Definition #1
        obj_td = cls.env["tier.definition"]
        cls.td = obj_td.create(
            {
                "name": "Tier Validation Tester",
                "model_id": cls.tester_model.id,
                "python_code": "True",
                "sequence": 1,
            }
        )

        obj_td_review = cls.env["tier.definition.review"]
        cls.td_review = obj_td_review.create(
            {
                "definition_id": cls.td.id,
                "review_type": "individual",
                "reviewer_ids": [(6, 0, [cls.user1.id])],
            }
        )

        # Create Tier Definition #2
        cls.td_2 = obj_td.create(
            {
                "name": "Tier Validation Tester 2",
                "model_id": cls.tester_model.id,
                "python_code": "True",
                "sequence": 2,
            }
        )
        cls.td_review_2 = obj_td_review.create(
            {
                "definition_id": cls.td_2.id,
                "review_type": "individual",
                "reviewer_ids": [(6, 0, [cls.user1.id, cls.user3.id])],
            }
        )

        cls.test_data = cls.test_model.create(
            {
                "name": "Data 01",
            }
        )
        cls.test_data_2 = cls.test_model.create(
            {
                "name": "Data 02",
                "definition_id": cls.td_2.id,
            }
        )

    @classmethod
    def tearDownClass(cls):
        teardown_test_model(cls.env, [TierValidationTester])
        super(TierValidationTest, cls).tearDownClass()

    def test_01(self):
        """Normal Validation"""
        self.assertFalse(self.test_data.definition_id.id)
        record = self.test_data.with_user(self.user1)
        record_2 = self.test_data.with_user(self.user2)
        self.assertFalse(
            record_2.definition_id.id,
        )
        record_2.action_confirm()
        record_2.invalidate_cache()
        self.assertEqual(
            record_2.state,
            "confirm",
        )
        self.assertTrue(
            record_2.review_ids,
        )
        record.validate_tier()
        self.assertTrue(record.validated)

    def test_02(self):
        """User 2 try to validate"""
        self.assertFalse(self.test_data.definition_id.id)
        record_2 = self.test_data.with_user(self.user2)
        self.assertFalse(
            record_2.definition_id.id,
        )
        record_2.action_confirm()
        record_2.invalidate_cache()
        self.assertEqual(
            record_2.state,
            "confirm",
        )
        self.assertTrue(
            record_2.review_ids,
        )
        record_2.validate_tier()
        self.assertFalse(record_2.validated)

    def test_03(self):
        """User 2 reject and restart validation"""
        self.assertFalse(self.test_data.definition_id.id)
        record = self.test_data.with_user(self.user1)
        record_2 = self.test_data.with_user(self.user2)
        self.assertFalse(
            record_2.definition_id.id,
        )
        record_2.action_confirm()
        record_2.invalidate_cache()
        self.assertEqual(
            record_2.state,
            "confirm",
        )
        self.assertTrue(
            record_2.review_ids,
        )
        record.reject_tier()
        self.assertTrue(record.rejected)
        record.restart_validation()
        self.assertFalse(record.review_ids)

    def test_04(self):
        """Normal Validation with 2 Reviewers"""
        record_2 = self.test_data_2.with_user(self.user2.id)
        record_3 = self.test_data_2.with_user(self.user3.id)
        record_2.invalidate_cache()
        self.assertEqual(
            record_2.definition_id.id,
            self.td_2.id,
        )
        self.assertEqual(
            record_2.definition_id.definition_review_ids.reviewer_ids,
            self.td_2.definition_review_ids.reviewer_ids,
        )
        record_2.action_confirm()
        record_2.invalidate_cache()
        self.assertEqual(
            record_2.state,
            "confirm",
        )
        self.assertTrue(
            record_2.review_ids,
        )
        record_3.validate_tier()
        self.assertTrue(record_3.validated)
