# Generated by Django 4.2.4 on 2023-08-30 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apikey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apikey',
            name='token',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]