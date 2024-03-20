# Generated by Django 4.2.11 on 2024-03-20 14:19

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0008_alter_reservation_booking_date_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="reservation",
            options={
                "ordering": ["booking_date", "booking_time", "guest_count", "entry_id"]
            },
        ),
        migrations.AlterField(
            model_name="reservation",
            name="booking_date",
            field=models.DateField(
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=datetime.date(2024, 3, 20)
                    )
                ]
            ),
        ),
    ]