# Generated by Django 5.1.5 on 2025-03-29 06:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DPDM2', '0008_remove_missing_vehicle_station_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='missing_vehicle',
            name='station_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='DPDM2.station'),
            preserve_default=False,
        ),
    ]
