# Generated by Django 4.2.4 on 2023-08-31 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apikey', '0004_alter_apikey_usage_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apikey',
            old_name='usage_rate',
            new_name='throttle_rate',
        ),
    ]