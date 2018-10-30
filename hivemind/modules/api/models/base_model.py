"""
Base Model for Api Module
"""
from django.db import models


class BaseModel(models.Model):
    """
    This is the Base Model.
    """
    created = models.DateTimeField(
        'Created',
        help_text=f'The date and time on which the object was created.',
        auto_now_add=True)
    modified = models.DateTimeField(
        'Modified',
        help_text='The date and time on which the object was last modified.',
        auto_now=True)

    # pylint: disable=too-few-public-methods
    class Meta:
        """
        Meta Options for the Base Model.
        """
        abstract = True
