# Generated by Django 4.1.7 on 2023-09-21 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='index',
        ),
    ]
