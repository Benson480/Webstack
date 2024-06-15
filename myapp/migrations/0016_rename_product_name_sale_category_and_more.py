# Generated by Django 5.0.4 on 2024-05-07 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_remove_sale_sales_integer_amount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='product_name',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='sale',
            old_name='quantity_sold',
            new_name='cost',
        ),
        migrations.RenameField(
            model_name='sale',
            old_name='sales_amount',
            new_name='date',
        ),
        migrations.AddField(
            model_name='sale',
            name='day',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='month',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='week',
            field=models.TextField(blank=True, null=True),
        ),
    ]