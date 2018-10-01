"""
Tests for API Module Signals
"""
import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase
from model_mommy import mommy

from hivemind.modules.api.models import Profile
from hivemind.modules.api.models.event import Event


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

    def test_event_clean(self):
        """
        Test that when an event is created that
        the dates are properly set and validated.
        """

        timezone = datetime.timezone(datetime.timedelta(0))

        # End time before start time
        with self.assertRaises(ValidationError):
            Event(name='Test',
                  description='Test',
                  start_time=datetime.datetime.now(tz=timezone),
                  end_time=datetime.datetime.now(tz=timezone) - datetime.timedelta(days=1)
                  ).clean()

        # End time after start time
        Event(name='Test',
              description='Test',
              start_time=datetime.datetime.now(tz=timezone),
              end_time=datetime.datetime.now(tz=timezone) + datetime.timedelta(days=1)
              ).clean()
