# Generated by Django 5.1.2 on 2024-10-31 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventCalendar', '0005_alter_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='ages',
            field=models.CharField(blank=True, max_length=120, verbose_name='Ages'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(blank=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='exclude',
            field=models.BooleanField(blank=True, verbose_name='Exclude from Weekly'),
        ),
        migrations.AlterField(
            model_name='event',
            name='link',
            field=models.URLField(blank=True, max_length=500, verbose_name='EventInfo'),
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, verbose_name='Ticket Price'),
        ),
        migrations.AlterField(
            model_name='event',
            name='sold_out',
            field=models.BooleanField(blank=True, verbose_name='Sold Out'),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.CharField(blank=True, max_length=120, verbose_name='Time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.CharField(blank=True, max_length=120, verbose_name='Venue'),
        ),
    ]
