# Generated by Django 4.2.4 on 2023-09-02 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apikey', '0005_rename_usage_rate_apikey_throttle_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apikey',
            old_name='throttle_rate',
            new_name='usage_rate',
        ),
    ]