# Generated by Django 5.0.7 on 2024-10-01 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommers', '0045_rename_id_admininfo_a_id_rename_id_category_c_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
