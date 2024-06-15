# Generated by Django 5.0.4 on 2024-04-25 11:07

import myapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_item_price_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('quantity_sold', models.IntegerField()),
                ('sales_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='itemimage',
            name='status',
            field=models.CharField(choices=(('default', 'Select availability...'), ('available', 'Available now'), ('Service available', ' Service Available now'), ('Course available', 'Course available'), ('Out of Stock', 'Out of Stock'), ('future', myapp.models.ItemImage.availability_description)), db_index=True, max_length=255, null=True),
        ),
    ]