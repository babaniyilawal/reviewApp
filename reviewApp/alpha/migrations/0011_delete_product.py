# Generated by Django 4.1.7 on 2023-04-05 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0010_alter_product_date_released'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
