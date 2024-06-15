# Generated by Django 5.0.4 on 2024-06-11 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_sale_category_alter_sale_cost_alter_sale_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_alumni', models.BooleanField(default=False)),
                ('alumni_certificate', models.FileField(blank=True, null=True, upload_to='certificates/')),
            ],
        ),
    ]