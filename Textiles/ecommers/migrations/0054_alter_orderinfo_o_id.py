# Generated by Django 5.1.2 on 2024-10-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommers', '0053_orderinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='o_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
