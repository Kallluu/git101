# Generated by Django 5.1.5 on 2025-04-06 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DPDM2', '0021_assign_fund_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assign_fund',
            name='fund_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DPDM2.fund'),
        ),
    ]
