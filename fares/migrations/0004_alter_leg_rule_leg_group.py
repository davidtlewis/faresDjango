# Generated by Django 4.1.1 on 2022-10-25 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fares', '0003_leg_group_ref_id_alter_leg_group_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leg_rule',
            name='leg_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fares.leg_group'),
        ),
    ]
