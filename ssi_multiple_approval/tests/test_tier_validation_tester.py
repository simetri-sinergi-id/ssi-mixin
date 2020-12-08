# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo.exceptions import UserError, ValidationError
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

        # Create Tier Definition
        obj_td = cls.env["tier.definition"]
        cls.td = obj_td.create(
            {
                "name": "Tier Validation Tester",
                "model_id": cls.tester_model.id,
                "python_code": "True",
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

        cls.test_data = cls.test_model.create(
            {
                "name": "Data 01",
            }
        )

    @classmethod
    def tearDownClass(cls):
        teardown_test_model(cls.env, [TierValidationTester])
        super(TierValidationTest, cls).tearDownClass()

    def test_01(self):
        self.assertFalse(self.test_data.definition_id.id)

        record = self.test_data.with_user(self.user1)
        record.action_confirm()

        # Check State == "confirm"
        self.assertEqual(
            record.state,
            "confirm",
        )

        reviews = record.request_validation()

        # Check Tier Definition
        self.assertEqual(
            record.definition_id.id,
            self.td.id,
        )
