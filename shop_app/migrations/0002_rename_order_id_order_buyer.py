# Generated by Django 4.2.5 on 2023-09-27 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_id',
            new_name='buyer',
        ),
    ]
