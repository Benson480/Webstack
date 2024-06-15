# Generated by Django 5.0.4 on 2024-04-18 13:38

import myapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_career_jobapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_price',
            name='Unit_Of_Measure',
            field=models.CharField(choices=[('Kg', 'Kg'), ('Ltr', 'Ltr'), ('Bag', 'Bag'), ('Pcs', 'Pcs'), ('Pcs', 'Pc'), ('Carton', 'Carton'), ('Pkt', 'Pkt'), ('Tons', 'Tons'), ('Bottles', 'Bottles'), ('Dose', 'Dose'), ('Course', 'Course'), ('Square Meter', 'Square Meter'), ('Case', 'Case'), ('Custom Software', 'Custom Software')], db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='itemimage',
            name='status',
            field=models.CharField(choices=(('default', 'Select availability...'), ('available', 'Available now'), ('Service available', ' Service Available now'), ('Out of Stock', 'Out of Stock'), ('future', myapp.models.ItemImage.availability_description)), db_index=True, max_length=255, null=True),
        ),
    ]