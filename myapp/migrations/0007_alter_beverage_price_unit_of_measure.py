# Generated by Django 4.1.7 on 2024-03-25 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_announcement_image_announcement_image_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beverage_price',
            name='Unit_Of_Measure',
            field=models.CharField(choices=[('Kg', 'Kg'), ('Ltr', 'Ltr'), ('Bag', 'Bag'), ('Pcs', 'Pcs'), ('Pcs', 'Pc'), ('Carton', 'Carton'), ('Pkt', 'Pkt'), ('Tons', 'Tons'), ('Bottles', 'Bottles'), ('Dose', 'Dose'), ('Course', 'Course'), ('Square Meter', 'Square Meter')], db_index=True, max_length=255, null=True),
        ),
    ]
