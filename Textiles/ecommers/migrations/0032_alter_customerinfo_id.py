# Generated by Django 5.0.7 on 2024-10-01 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommers', '0031_customerinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinfo',
            name='id',
            field=models.CharField(editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
