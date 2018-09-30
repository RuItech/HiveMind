"""
User Profile Model For API Module
"""
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    """
    This is a Users Profile. Provides Extra Details
    On a User
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(
        'First Name',
        max_length=255,
        help_text='This Represents the Users First Name.')
    last_name = models.CharField(
        'Last Name',
        max_length=255,
        help_text='This Represents the Users Last Name.')
    school_id = models.CharField(
        'School ID',
        max_length=20,
        unique=True,
        help_text='This Represents the Users School ID.')
    email = models.EmailField(
        'Email',
        unique=True,
        help_text='This Represents the Users Email.'
    )
    phone_number = PhoneNumberField(
        'Phone Number',
        blank=True,
        help_text='This Represents the Users Phone Number.'
    )

    # pylint: disable=too-few-public-methods
    class Meta:
        """
        Meta Options for UserProfile Class
        """

        ordering = ['id', 'school_id', 'last_name']

    def __str__(self):
        """
        String Representation for StudentProfile Object
        """
        return f"{self.school_id} - {self.last_name}, {self.first_name}"


# pylint: disable=unused-argument
def create_profile(sender, instance, created, **kwargs):
    """
    Signal that is called when a USER is Created. Creates
    a Profile for the User
    """
    if created:
        Profile.objects.create(  # pylint: disable=no-member
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email)


post_save.connect(
    create_profile, sender=User, dispatch_uid='create_profile')
