# Generated by Django 4.1.7 on 2023-09-19 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_employee_index_alter_employer_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_usage',
            name='Place_of_usage',
            field=models.CharField(choices=[('Internal', 'Internal')], db_index=True, max_length=255, null=True),
        ),
    ]