# Generated by Django 5.0.2 on 2024-02-12 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_flight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='airline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='flight_airline', to='core.airline'),
        ),
        migrations.AlterField(
            model_name='runway',
            name='airport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='runway_airport', to='core.airport'),
        ),
    ]
