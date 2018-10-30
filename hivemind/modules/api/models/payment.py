"""
Payment Model for API Module
"""
from django.db import models

from .base_model import BaseModel
from .profile import Profile


class Payment(BaseModel):
    """
    Payment Model
    """
    owner = models.ForeignKey(
        Profile, on_delete=models.SET_DEFAULT, default=None, null=True)
    payment_ref = models.CharField(
        'Payment Reference',
        max_length=50,
        help_text='Represents Payment Reference.')
    extra_info = models.TextField(
        'Extra Info',
        blank=True,
        default="",
        help_text='Represent extra information related to Payment.')

    # pylint: disable=too-few-public-methods
    class Meta():
        """
        Meta Options for Payment Model
        """
        ordering = ['id', 'owner']

    def __str__(self):
        """
        String Representation for Payment Model
        """
        return self.payment_ref
