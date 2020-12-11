from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import YP_General_Information, YP_Contact_Info, Profile_Pic, YP_Health_And_Wellness, YP_Physical_Description, \
    YP_Banking_Information, YP_Pen_Pic, YP_Profile_Child, YP_IPA, YP_Relationships_Associates


@receiver(post_save, sender=YP_General_Information)
def add_genaral_information(sender, instance, created, **kwargs):
    if created:
        Profile_Pic.objects.create(yp=instance)
        YP_Contact_Info.objects.create(yp=instance)
        YP_Health_And_Wellness.objects.create(yp=instance)
        YP_Physical_Description.objects.create(yp=instance)
        YP_Banking_Information.objects.create(yp=instance)
        YP_Pen_Pic.objects.create(yp=instance)
        YP_Profile_Child.objects.create(yp=instance)
        YP_IPA.objects.create(yp=instance)
        YP_Relationships_Associates.objects.create(yp=instance)


@receiver (post_save, sender=YP_General_Information)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
