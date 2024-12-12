# Generated by Django 5.0.7 on 2024-09-19 08:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommers', '0025_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email_id', models.EmailField(max_length=255)),
                ('quantity', models.IntegerField(default=1)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommers.product')),
            ],
        ),
    ]
