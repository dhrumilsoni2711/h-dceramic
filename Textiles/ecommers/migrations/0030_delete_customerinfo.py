# Generated by Django 5.0.7 on 2024-10-01 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommers', '0029_rename_u_country_customerinfo_u_city'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomerInfo',
        ),
    ]
