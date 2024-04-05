# Generated by Django 5.0.4 on 2024-04-04 08:09

import myapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimage',
            name='status',
            field=models.CharField(choices=(('default', 'Select availability...'), ('available', 'Available now'), ('Out of Stock', 'Out of Stock'), ('future', myapp.models.ItemImage.availability_description)), db_index=True, max_length=255, null=True),
        ),
    ]