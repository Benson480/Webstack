# Generated by Django 4.1.7 on 2023-09-27 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_contactdetails_department_contact_details'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactDetails',
            new_name='ContactDetail',
        ),
    ]