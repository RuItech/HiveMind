"""
User Profile Model For API Module
"""
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    """
    This is a Users Profile. Provides Extra Details
    On a User
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    prefix = models.CharField(
        'Prefix',
        max_length=10,
        blank=True,
        help_text='Your prefix such as Mr. or Ms.'
    )
    first_name = models.CharField(
        'First Name',
        max_length=255,
        help_text='This Represents the Users First Name.'
    )
    preposition = models.CharField(
        'Preposition',
        max_length=255,
        blank=True,
        help_text='Your family name preposition.'
    )
    last_name = models.CharField(
        'Last Name',
        max_length=255,
        help_text='This Represents the Users Last Name.'
    )

    school_id = models.CharField(
        'School ID',
        max_length=20,
        unique=True,
        help_text='This Represents the Users School ID.'
    )

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

    def get_full_name(self):
        """
        Returns the full name of the person
        """
        if self.preposition:
            return f"{self.first_name} {self.preposition} {self.last_name}"

        return f"{self.first_name} {self.last_name}"

    def get_last_name(self):
        """
        Returns the last name of the person.
        """
        if self.preposition:
            return f"{self.last_name}, {self.preposition}"

        return self.last_name

    def get_first_name(self):
        """
        Returns the first name of the person.
        """
        return self.first_name

    def __str__(self):
        """
        String Representation for StudentProfile Object
        """
        return f"{self.school_id} - {self.get_full_name()}"


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
