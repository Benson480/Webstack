# Generated by Django 4.1.7 on 2023-10-31 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_activity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='details',
            new_name='description',
        ),
        migrations.AddField(
            model_name='activity',
            name='user_logout',
            field=models.BooleanField(default=False),
        ),
    ]