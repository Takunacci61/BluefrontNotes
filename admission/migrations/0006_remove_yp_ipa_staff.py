# Generated by Django 3.1.3 on 2020-12-05 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0005_yp_banking_information_yp_health_and_wellness_yp_ipa_yp_pen_pic_yp_physical_description_yp_profile_c'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yp_ipa',
            name='staff',
        ),
    ]