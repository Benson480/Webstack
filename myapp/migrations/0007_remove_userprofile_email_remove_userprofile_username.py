# Generated by Django 4.1.7 on 2023-09-25 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_userprofile_email_userprofile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
    ]