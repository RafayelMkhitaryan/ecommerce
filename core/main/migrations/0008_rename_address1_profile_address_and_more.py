# Generated by Django 5.1.5 on 2025-02-13 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_profile_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='address1',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='address2',
        ),
    ]
