# Generated by Django 4.1.7 on 2023-02-21 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fares', '0028_rename_legacy_amount_leg_rule_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leg_rule',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]