# Generated by Django 4.1.7 on 2023-02-21 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fares', '0026_alter_transfer_rule_fare_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='leg_rule',
            name='legacy_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
