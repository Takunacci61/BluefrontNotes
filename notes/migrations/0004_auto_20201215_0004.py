# Generated by Django 3.1.3 on 2020-12-15 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_parent_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='parent_notes',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
