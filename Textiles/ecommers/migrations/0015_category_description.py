# Generated by Django 5.0.7 on 2024-09-17 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommers', '0014_alter_customerinfo_u_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
