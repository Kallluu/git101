# Generated by Django 5.1.5 on 2025-05-07 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DPDM2', '0037_alter_fund_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='duty_assignment',
            name='completed',
            field=models.IntegerField(default=0),
        ),
    ]
