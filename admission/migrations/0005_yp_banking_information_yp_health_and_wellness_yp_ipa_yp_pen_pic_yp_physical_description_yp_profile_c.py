# Generated by Django 3.1.3 on 2020-12-05 17:06

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admission', '0004_yp_contact_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='YP_Profile_Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yp_streghts', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('yp_achivements', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('yp_hobbies', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('personality', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('yp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admission.yp_general_information')),
            ],
            options={
                'verbose_name_plural': 'Young Person Contact Information',
            },
        ),
        migrations.CreateModel(
            name='YP_Physical_Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yp_height', models.IntegerField(default=0)),
                ('yp_weight', models.IntegerField(default=0)),
                ('yp_build', models.CharField(choices=[('Fat', 'Fat'), ('Stocky', 'Stocky'), ('Prop', 'Prop'), ('Thin', 'Thin'), ('Slight', 'Slight'), ('Heavy', 'Heavy'), ('Broad', 'Broad'), ('Medium', 'Medium'), ('Slim', 'Slim'), ('Small', 'Small')], default='Slim', max_length=10)),
                ('yp_complexion', models.CharField(max_length=100)),
                ('yp_eye_colour', models.CharField(max_length=100)),
                ('yp_hair_colour', models.CharField(max_length=100)),
                ('yp_marks_scars_tattoos', models.CharField(max_length=100)),
                ('yp_disabilities', models.CharField(max_length=100)),
                ('yp_relevant_medical_information', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('yp_medications', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('yp_date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('yp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admission.yp_general_information')),
            ],
            options={
                'verbose_name_plural': 'Young Person Physical Description',
            },
        ),
        migrations.CreateModel(
            name='YP_Pen_Pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yp_pen_picture', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('yp_pen_picture_background', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('yp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admission.yp_general_information')),
            ],
            options={
                'verbose_name_plural': 'Young Person Pen Picture',
            },
        ),
        migrations.CreateModel(
            name='YP_IPA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yp_placement_start_date', models.DateField(default=django.utils.datetime_safe.date.today)),
                ('yp_initial_ipa_received_date', models.DateField(default=django.utils.datetime_safe.date.today)),
                ('yp_last_ipa_start_date', models.DateField(default=django.utils.datetime_safe.date.today)),
                ('yp_proposed_placement_end_date', models.DateField(default=django.utils.datetime_safe.date.today)),
                ('yp_type_placement', models.CharField(max_length=100)),
                ('yp_date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('yp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ipa', to='admission.yp_general_information')),
            ],
            options={
                'verbose_name_plural': 'Young Person IPA',
            },
        ),
        migrations.CreateModel(
            name='YP_Health_And_Wellness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yp_ability_to_make_attachments', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('yp_food_allergies', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('yp_allergies_and_attitudes', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('yp_resilience_and_self_esteem', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('yp_substance_misuse_issues', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('yp_sexual_health', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('yp_Attitude_To_Food_And_Weight', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('yp_smoking', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('yp_personal_hygiene', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('yp_learning_difficulties', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('yp_physical_or_sensory_impairments_and_disabilities', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('yp_healthcare_professional_involvement', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('yp_date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('yp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admission.yp_general_information')),
            ],
            options={
                'verbose_name_plural': 'Young Person Health and Wellness',
            },
        ),
        migrations.CreateModel(
            name='YP_Banking_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yp_bank', models.CharField(max_length=100)),
                ('yp_bank_name', models.CharField(max_length=100)),
                ('yp_bank_sort_code', models.IntegerField(default=0)),
                ('yp_bank_account_number', models.IntegerField(default=0)),
                ('yp_date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('yp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admission.yp_general_information')),
            ],
            options={
                'verbose_name_plural': 'Young Person Banking Information',
            },
        ),
    ]