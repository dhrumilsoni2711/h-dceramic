# Generated by Django 5.0.7 on 2024-08-09 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommers', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pin_code',
            field=models.CharField(max_length=6),
        ),
    ]
