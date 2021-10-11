from django.contrib.auth.models import User
from django.db.models.signals import *
from django.dispatch import receiver


@receiver(pre_save, sender=User)
def user_email_lowercase(sender, instance, **kwargs):
    """
    Make user email lowercase
    """
    instance.email = instance.email.lower()
