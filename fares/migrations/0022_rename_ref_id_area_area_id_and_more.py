# Generated by Django 4.1.1 on 2022-11-28 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fares', '0021_rename_ref_id_network_area_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area',
            old_name='ref_id',
            new_name='area_id',
        ),
        migrations.RenameField(
            model_name='network',
            old_name='area_id',
            new_name='ref_id',
        ),
    ]
