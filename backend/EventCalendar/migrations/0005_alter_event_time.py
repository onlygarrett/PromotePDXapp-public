# Generated by Django 5.1.2 on 2024-10-31 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventCalendar', '0004_alter_event_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.CharField(max_length=120, verbose_name='Time'),
        ),
    ]
