# Generated by Django 4.2 on 2023-04-23 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_repairing_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=200),
        ),
    ]
