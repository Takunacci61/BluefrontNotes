from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.datetime_safe import date
from admission.models import YP_General_Information


class Notes(models.Model):
    OPTION_1 = 'Face-to-Face'
    OPTION_2 = 'Telephone'
    OPTION_3 = 'Email'
    OPTION_4 = 'Instant Messaging'
    OPTION_5 = 'Task'
    OPTION_6 = 'Admin'

    CONTACT_CHOICES = [
        (OPTION_1, 'Face-to-Face'),
        (OPTION_2, 'Telephone'),
        (OPTION_3, 'Email'),
        (OPTION_4, 'Instant Messaging'),
        (OPTION_5, 'Task'),
        (OPTION_6, 'Admin'),

    ]

    yp = models.ForeignKey(YP_General_Information, related_name="notes", on_delete=models.CASCADE)
    date_notes = models.DateField(default=date.today)
    time_start = models.TimeField(auto_now=False, auto_now_add=False)
    time_end = models.TimeField(auto_now=False, auto_now_add=False)
    location_id = models.CharField(max_length=100)
    contact_type = models.CharField(max_length=100, choices=CONTACT_CHOICES ,default=OPTION_1)
    staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    detailed_notes = RichTextField(blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Young Person Notes"

    def __str__(self):
        return f'{self.yp}  Notes Taken On  {self.date_notes}'

    def get_absolute_url(self):
        return reverse('notes-detail', kwargs={'pk': self.pk})

