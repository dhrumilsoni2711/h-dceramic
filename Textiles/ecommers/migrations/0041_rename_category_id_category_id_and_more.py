# Generated by Django 5.0.7 on 2024-10-01 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommers', '0040_alter_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
    ]
