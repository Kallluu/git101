# Generated by Django 5.1.5 on 2025-04-02 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DPDM2', '0014_fund_allocation_delete_vehicleinsurance'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='fund_allocation',
            new_name='fund',
        ),
    ]
