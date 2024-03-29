# Generated by Django 4.1.7 on 2024-03-25 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_beverage_price_unit_of_measure'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='announcement_images/'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='image_description',
            field=models.CharField(blank=True, help_text='Description of the image', max_length=255, null=True),
        ),
    ]
