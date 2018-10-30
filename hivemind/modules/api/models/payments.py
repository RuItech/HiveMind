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
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL)
    payment_ref = models.CharField(
        'Payment Reference',
        max_length=50,
        help_text='Represents Payment Reference.')
    extra_info = models.TextField(
        'Extra Info',
        blank=True,
        default=None,
        help_text='Represent extra information related to Payment.')

    class Meta():
        """
        Meta Options for Payment Model
        """
        ordering = ['id', 'owner']

    def __str__(self):
        """
        String Representation for Payment Model
        """
        return f"{self.payment_ref} - {self.created}"
