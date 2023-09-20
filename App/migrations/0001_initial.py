# Generated by Django 4.2.4 on 2023-09-20 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('teacher', 'Teacher'), ('student', 'Student'), ('panchayat', 'Panchayat'), ('volunteer', 'Volunteer'), ('donator', 'Donator'), ('other', 'Other')], max_length=100)),
                ('subject', models.CharField(max_length=500)),
                ('message', models.TextField()),
            ],
        ),
    ]