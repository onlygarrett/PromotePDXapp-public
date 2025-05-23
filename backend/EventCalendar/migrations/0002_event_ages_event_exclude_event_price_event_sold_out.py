# Generated by Django 5.1.2 on 2024-10-31 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventCalendar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='ages',
            field=models.CharField(default='', max_length=120, verbose_name='Ages'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='exclude',
            field=models.BooleanField(default=False, verbose_name='Exclude from Weekly'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Ticket Price'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='sold_out',
            field=models.BooleanField(default=False, verbose_name='Sold Out'),
            preserve_default=False,
        ),
    ]
