# Generated by Django 5.1.5 on 2025-05-07 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DPDM2', '0036_remove_station_authentication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
