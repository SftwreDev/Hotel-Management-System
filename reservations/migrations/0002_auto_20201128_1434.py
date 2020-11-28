# Generated by Django 3.1.3 on 2020-11-28 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='rates',
            field=models.DecimalField(decimal_places=2, default=1500, max_digits=10, verbose_name='Rates per Room'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checkinandout',
            name='check_in',
            field=models.BooleanField(default=False, help_text='Check if check in , uncheck if check out', verbose_name='Checking In or Out?'),
        ),
    ]
