# Generated by Django 4.1.7 on 2023-02-21 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fares', '0030_calendar'),
    ]

    operations = [
        migrations.AddField(
            model_name='leg_rule',
            name='service_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fares.calendar'),
        ),
    ]
