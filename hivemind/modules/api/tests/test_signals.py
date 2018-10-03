"""
Tests for API Module Signals
"""
from django.test import TestCase
from model_mommy import mommy

from hivemind.modules.api.models import Profile


class TestSignals(TestCase):
    """
    Test API Module Signals
    """

    def test_user_creates_profile(self):
        """
        Test that when a User is created a
        Profile is created for the User
        """

        # Confirm no Profile Exists at Start
        # pylint: disable=no-member
        self.assertEqual(0, Profile.objects.all().count())

        user = mommy.make('auth.User', username='Bobby')
        # Confirm a Profile was created and is linked to Bobby
        self.assertEqual(1, Profile.objects.all().count())
        profile = Profile.objects.first()

        self.assertEqual(profile.user, user)
        self.assertEqual(profile.first_name, user.first_name)
        self.assertEqual(profile.last_name, user.last_name)
        self.assertEqual(profile.email, user.email)
