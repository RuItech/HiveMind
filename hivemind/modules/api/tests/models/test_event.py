"""
Tests for API Module Signals
"""
import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from hivemind.modules.api.models.event import Event


class TestEvent(TestCase):
    """
    Test for Event Model
    """

    def test_event_clean(self):
        """
        Test that when an event is created that
        the dates are properly set and validated.
        """

        timezone = datetime.timezone(datetime.timedelta(0))
        now = datetime.datetime.now(tz=timezone)

        # End time before start time
        with self.assertRaises(ValidationError):
            Event(name='Test',
                  description='Test',
                  start_time=now,
                  end_time=now - datetime.timedelta(days=1)
                  ).clean()

        # End time same as start time
        with self.assertRaises(ValidationError):
            Event(name='Test',
                  description='Test',
                  start_time=now,
                  end_time=now
                  ).clean()

        # End time after start time
        Event(name='Test',
              description='Test',
              start_time=now,
              end_time=now + datetime.timedelta(days=1)
              ).clean()
