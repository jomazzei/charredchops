# Generated by Django 4.2.11 on 2024-03-13 15:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='guest_count',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(1)]),
        ),
    ]