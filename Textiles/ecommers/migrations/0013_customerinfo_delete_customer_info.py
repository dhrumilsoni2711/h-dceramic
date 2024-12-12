# Generated by Django 5.0.7 on 2024-08-15 06:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommers', '0012_delete_userpassword'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.CharField(editable=False, max_length=10, unique=True)),
                ('u_name', models.CharField(max_length=50)),
                ('u_email', models.EmailField(max_length=254, unique=True)),
                ('u_phone_number', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be 10 digits.', regex='^\\d{10}$')])),
                ('u_street_address', models.CharField(max_length=100)),
                ('u_state', models.CharField(max_length=50)),
                ('u_country', models.CharField(max_length=50)),
                ('u_pin_code', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Pin code must be 6 digits.', regex='^\\d{6}$')])),
                ('u_password', models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(8, message='Password must be at least 8 characters long.')])),
            ],
        ),
        migrations.DeleteModel(
            name='customer_info',
        ),
    ]