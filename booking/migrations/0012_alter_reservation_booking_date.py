# Generated by Django 4.2.11 on 2024-03-24 11:50

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0011_alter_reservation_booking_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="booking_date",
            field=models.DateField(
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=datetime.date(2024, 3, 24)
                    )
                ]
            ),
        ),
    ]
