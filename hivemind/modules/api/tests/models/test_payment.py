"""
Tests for Payment Model
"""
from django.test import TestCase
from model_mommy import mommy


class TestPayment(TestCase):
    """
    Tests for Payment Model
    """

    def test_model_str_representation(self):
        """
        Test Payment String Representation.

        Expected Representation Format: C00001
        """
        payment = mommy.make('api.Payment', payment_ref='C00001', owner=None)

        self.assertEqual(str(payment), f'C00001')
