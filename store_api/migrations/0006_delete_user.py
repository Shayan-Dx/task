# Generated by Django 4.2.2 on 2023-08-14 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_api', '0005_remove_product_categories_product_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
