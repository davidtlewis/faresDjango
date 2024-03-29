# Generated by Django 4.1.1 on 2022-10-27 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fares', '0013_product_ref_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='ref_id',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='fare_container',
            name='currency',
            field=models.CharField(default='USD', max_length=3),
        ),
        migrations.AlterField(
            model_name='leg_rule',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leg_rules', to='fares.product'),
        ),
        migrations.AlterField(
            model_name='network',
            name='ref_id',
            field=models.CharField(max_length=128),
        ),
    ]
