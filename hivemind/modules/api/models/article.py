"""
Article Model for API Module.
"""
from django.db import models

from hivemind.modules.api.models.base_model import BaseModel


class Article(BaseModel):
    """
    This is the Article Model.
    """
    headline = models.CharField(
        'Headline',
        max_length=255,
        help_text='The headline of the article.',
    )
    content = models.TextField(
        'Content',
        help_text='The contents of the article.',
    )

    def __str__(self):
        """
        String representation for the Article Model.
        """
        return f"{self.headline}"

    # pylint: disable=too-few-public-methods
    class Meta:
        """
        Meta options for the Article Class.
        """
        ordering = ['created', 'headline']
