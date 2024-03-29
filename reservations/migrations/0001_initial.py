# Generated by Django 3.1.2 on 2020-12-16 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('room_type', models.CharField(choices=[('Single Bed Size Room', 'Single Bed Size Room'), ('Double Bed Size Room', 'Double Bed Size Room'), ('Family Bed Size Room', 'Family Bed Size Room')], max_length=100, verbose_name='Type of Room')),
                ('room_no', models.PositiveIntegerField(help_text='Should be unique and not existing room no', unique=True, verbose_name='Room No')),
                ('rates', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Rates per Room')),
                ('available', models.BooleanField(default=False, verbose_name='Reserved')),
            ],
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Customer Name')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('email_address', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('contact', models.CharField(max_length=255, verbose_name='Contact No')),
                ('type_of_id', models.CharField(max_length=255, verbose_name='Type of ID')),
                ('id_no', models.CharField(max_length=255, verbose_name='ID No')),
                ('no_of_days', models.PositiveIntegerField(max_length=255, verbose_name='No of Days')),
                ('check_in_datetime', models.DateTimeField(verbose_name='Date & Time for Check In')),
                ('check_out_datetime', models.DateTimeField(verbose_name='Date & Time for Check Out')),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_user', to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='room_type_and_no', to='reservations.room', verbose_name='Room Type & No')),
            ],
        ),
        migrations.CreateModel(
            name='CheckInAndOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.BooleanField(default=False, help_text='Check if check in , uncheck if check out', verbose_name='Checking In or Out?')),
                ('check_in_date_time', models.DateTimeField()),
                ('reservations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.reservations', verbose_name="Customer's Reservations")),
            ],
        ),
    ]
