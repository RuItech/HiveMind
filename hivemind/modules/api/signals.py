"""
Signals Module for API Module
"""
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from hivemind.modules.api.models import Profile


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
