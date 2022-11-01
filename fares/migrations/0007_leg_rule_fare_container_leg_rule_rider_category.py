# Generated by Django 4.1.1 on 2022-10-25 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fares', '0006_remove_area_name_remove_network_name_area_ref_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leg_rule',
            name='fare_container',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fares.fare_container'),
        ),
        migrations.AddField(
            model_name='leg_rule',
            name='rider_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fares.rider_category'),
        ),
    ]
