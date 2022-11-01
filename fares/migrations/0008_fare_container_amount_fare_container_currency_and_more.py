# Generated by Django 4.1.1 on 2022-10-25 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fares', '0007_leg_rule_fare_container_leg_rule_rider_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='fare_container',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fare_container',
            name='currency',
            field=models.CharField(default='USD', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fare_container',
            name='notes',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='fare_container',
            name='rider_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fares.rider_category'),
        ),
        migrations.AddField(
            model_name='rider_category',
            name='notes',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='transfer_rule',
            name='notes',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
