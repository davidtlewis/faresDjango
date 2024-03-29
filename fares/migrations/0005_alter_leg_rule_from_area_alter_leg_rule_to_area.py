# Generated by Django 4.1.1 on 2022-10-25 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fares', '0004_alter_leg_rule_leg_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leg_rule',
            name='from_area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area_to', to='fares.area'),
        ),
        migrations.AlterField(
            model_name='leg_rule',
            name='to_area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area_from', to='fares.area'),
        ),
    ]
