# Generated by Django 4.2.7 on 2023-11-28 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movers', '0005_service_available_areas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='booking_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
