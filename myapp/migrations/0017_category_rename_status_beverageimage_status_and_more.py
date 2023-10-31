# Generated by Django 4.1.7 on 2023-10-09 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_beverageimage_date_beverageimage_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='beverageimage',
            old_name='Status',
            new_name='status',
        ),
        migrations.AddField(
            model_name='beverageimage',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='images', to='myapp.category'),
        ),
    ]