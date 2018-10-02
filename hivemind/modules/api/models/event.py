"""
Event Model for API Module
"""
from django.core.exceptions import ValidationError
from django.db import models


class Event(models.Model):
    """
    This is the Event Model.
    """
    name = models.CharField(
        'Event Name',
        max_length=255,
        help_text='This represents the name of the event.'
    )
    description = models.TextField(
        'Event Description',
        help_text='This represents a (short) description of the event.'
    )

    start_time = models.DateTimeField(
        'Start Time',
        help_text='This is the time when the event starts.'
    )
    end_time = models.DateTimeField(
        'End Time',
        help_text='This is the time when the event ends.'
    )

    def __str__(self):
        """
        String representation for the Event Object
        """
        return f"{self.name}: {self.start_time} - {self.end_time}"

    def clean(self):
        # Validate that start_time and end_time are not the same
        # and that the start_time occurs before the end_time.
        if self.start_time >= self.end_time:
            raise ValidationError({
                'start_time': ValidationError(
                    'Start time should be before the end time.', code='invalid'
                ),
                'end_time':   ValidationError(
                    'Start time should be before the end time.', code='invalid'
                ),
            })

    # pylint: disable=too-few-public-methods
    class Meta:
        """
        Meta Options for the Event Class.
        """

        ordering = ['start_time', 'name', 'description']
