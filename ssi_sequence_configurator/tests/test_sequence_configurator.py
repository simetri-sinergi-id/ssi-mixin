# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo.tests.common import SavepointCase, tagged
from datetime import date
from .common import setup_test_model, teardown_test_model
from .model_configurator_tester import (
    ModelConfiguratorTester,
    ModelConfiguratorTesterType,
)


@tagged("post_install", "-at_install")
class ConfiguratorTester(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(ConfiguratorTester, cls).setUpClass()

        setup_test_model(
            cls.env, [ModelConfiguratorTesterType, ModelConfiguratorTester]
        )

        cls.test_model = cls.env[ModelConfiguratorTester._name]
        cls.test_model_type = cls.env[ModelConfiguratorTesterType._name]

        cls.tester_model = cls.env["ir.model"].search(
            [("model", "=", "model.configurator.tester")]
        )
        cls.tester_model_type = cls.env["ir.model"].search(
            [("model", "=", "model.configurator.tester.type")]
        )

        # Access record:
        cls.env["ir.model.access"].create(
            {
                "name": "access.model.configurator.tester",
                "model_id": cls.tester_model.id,
                "perm_read": 1,
                "perm_write": 1,
                "perm_create": 1,
                "perm_unlink": 1,
            }
        )
        cls.env["ir.model.access"].create(
            {
                "name": "access.model.configurator.tester.type",
                "model_id": cls.tester_model_type.id,
                "perm_read": 1,
                "perm_write": 1,
                "perm_create": 1,
                "perm_unlink": 1,
            }
        )

        # Create Fallback Sequence
        cls.fall_sequence = cls.env["ir.sequence"].create(
            {
                "name": "Fallback Sequence Configurator Test",
                "code": "model.configurator.tester.fallback",
                "padding": 5,
                "prefix": "FALLSEQ/",
                "number_next": 1,
                "number_increment": 1,
            }
        )

        # Create Sequence
        cls.sequence = cls.env["ir.sequence"].create(
            {
                "name": "Sequence Configurator Test",
                "code": "model.configurator.tester",
                "padding": 5,
                "prefix": "SEQTEST/",
                "number_next": 1,
                "number_increment": 1,
            }
        )

        # Create Sequence Configurator
        obj_seq_conf = cls.env["base.sequence_configurator"]
        obj_ir_field = cls.env["ir.model.fields"]

        sequence_field_id = obj_ir_field.search(
            [
                ("model_id.model", "=", "model.configurator.tester"),
                ("name", "=", "name"),
            ]
        )

        cls.configurator_id = obj_seq_conf.create(
            {
                "model_id": cls.tester_model.id,
                "sequence_field_id": sequence_field_id.id,
                "fallback_sequence_id": cls.fall_sequence.id,
            }
        )

        obj_seq_conf_line = cls.env["base.sequence_configurator_line"]
        str_code = "result = document.tester_type_id.sequence_id"
        cls.configurator_line_id = obj_seq_conf_line.create(
            {
                "generator_id": cls.configurator_id.id,
                "sequence": 1,
                "sequence_computation_code": str_code,
            }
        )

        # Create Data Tester
        cls.test_data = cls.test_model.create(
            {
                "description": "Data Test 01",
            }
        )

        # Create Data Tester With Type
        cls.test_data_type = cls.test_model_type.create(
            {
                "name": "Data Type 01",
                "code": "TYPE01",
                "sequence_id": cls.sequence.id,
            }
        )
        cls.test_data_02 = cls.test_model.create(
            {
                "description": "Data Test 01",
                "tester_type_id": cls.test_data_type.id,
            }
        )

    @classmethod
    def tearDownClass(cls):
        teardown_test_model(
            cls.env, [ModelConfiguratorTesterType, ModelConfiguratorTester]
        )
        super(ConfiguratorTester, cls).tearDownClass()

    def test_01(self):
        """ No Sequence Defined """
        self.assertEqual(
            self.test_data.name,
            "FALLSEQ/00001",
        )

    def test_02(self):
        """ Sequence Defined """
        self.assertEqual(
            self.test_data_02.name,
            "SEQTEST/00001",
        )

    def test_03(self):
        """ With Prefix Suffix Computation """
        year = date.today().year
        self.sequence.write({"prefix": ""})
        str_code = "prefix = 'TEST/' + document.tester_type_id.code + '/'"
        self.configurator_line_id.write(
            {
                "prefix_suffix_computation": True,
                "prefix_computation_code": str_code,
                "suffix_computation_code": "suffix = '/%(year)s'",
            }
        )
        test_data = self.test_model.create(
            {
                "description": "Data Test 02",
                "tester_type_id": self.test_data_type.id,
            }
        )
        result = "TEST/TYPE01/00002/%s" % (year)
        self.assertEqual(
            test_data.name,
            result,
        )
