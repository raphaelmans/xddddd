# Generated by Django 3.2.7 on 2021-09-30 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('midterm', '0003_alter_customer_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='car_id',
            new_name='customer',
        ),
    ]
