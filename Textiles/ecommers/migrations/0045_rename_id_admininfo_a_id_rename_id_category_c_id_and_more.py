# Generated by Django 5.0.7 on 2024-10-01 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommers', '0044_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admininfo',
            old_name='id',
            new_name='a_id',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='id',
            new_name='c_id',
        ),
        migrations.RenameField(
            model_name='customerinfo',
            old_name='id',
            new_name='u_id',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='id',
            new_name='p_id',
        ),
    ]
