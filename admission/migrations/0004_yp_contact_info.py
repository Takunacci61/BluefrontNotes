# Generated by Django 3.1.3 on 2020-12-05 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0003_care_house_infomation_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='YP_Contact_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.IntegerField(default=0)),
                ('travel_card', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
                ('email_address', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100)),
                ('twitter', models.CharField(max_length=100)),
                ('snapchat', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
                ('other', models.CharField(max_length=100)),
                ('yp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admission.yp_general_information')),
            ],
            options={
                'verbose_name_plural': 'Young Person Contact Information',
            },
        ),
    ]
