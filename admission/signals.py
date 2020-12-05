from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import YP_General_Information, YP_Contact_Info, Profile


@receiver (post_save, sender=YP_General_Information)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(yp=instance)
        YP_Contact_Info.objects.create(yp=instance)


@receiver (post_save, sender=YP_General_Information)
def save_profile(sender, instance, **kwargs):
    instance.profile.save ()
