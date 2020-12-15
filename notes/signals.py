from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Notes


@receiver (pre_save, sender=Notes)
def my_handler(sender, instance, **kwargs):
    instance.duration = instance.time_end - instance.time_start
