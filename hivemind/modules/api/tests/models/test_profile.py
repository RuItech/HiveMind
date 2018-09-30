"""
Tests for Profile Model
"""
from django.test import TestCase
from model_mommy import mommy


class TestProfile(TestCase):
    """
    Tests for Profile Model
    """

    def test_model_str_representation(self):
        """
        Test Student Profile String Representation.

        Expected Representation Format: AD111365 - Raymond, Davis
        """

        user = mommy.make(
            'auth.User',
            username='Dave',
            first_name='Dave',
            last_name='Raymond')
        profile = user.profile
        profile.school_id = 'AD111365'

        self.assertEqual(str(profile), 'AD111365 - Raymond, Dave')
