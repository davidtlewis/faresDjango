# Generated by Django 4.1.3 on 2022-11-27 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fares', '0017_rename_name_route_route_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stop',
            name='parent_station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fares.stop'),
        ),
    ]