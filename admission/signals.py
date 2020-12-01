from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import  YP_General_Information
from .models import Profile


@receiver(post_save, sender=YP_General_Information)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=YP_General_Information)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()