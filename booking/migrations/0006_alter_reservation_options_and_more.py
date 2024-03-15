# Generated by Django 4.2.11 on 2024-03-15 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_remove_reservation_allergies'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ['entry_id', 'booking_date', 'booking_time', 'guest_count']},
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='cancelled',
        ),
    ]
