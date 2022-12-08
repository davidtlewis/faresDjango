# Generated by Django 4.1.3 on 2022-11-27 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fares', '0015_alter_product_ref_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_id', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('currency', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_id', models.CharField(max_length=128)),
                ('stop_name', models.CharField(max_length=128)),
                ('location_type', models.CharField(choices=[('0', 'Stop'), ('1', 'Station'), ('2', 'Entrance or Exit'), ('3', 'Generic Node'), ('4', 'Boarding Point')], default='0', max_length=1)),
                ('parent_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fares.stop')),
            ],
        ),
    ]