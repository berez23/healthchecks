from django.contrib.auth.models import User
from django.db.models.signals import *
from django.dispatch import receiver
from django.utils.text import slugify


@receiver(pre_save, sender=User)
def user_email_lowercase(sender, instance, **kwargs):
    """
    Make user email lowercase
    """
    instance.email = instance.email.lower()


@receiver(pre_save, sender=User)
def user_username_slugify(sender, instance, **kwargs):
    """
    Slugify username to avoid special characters
    """
    instance.username = slugify(instance.username)
