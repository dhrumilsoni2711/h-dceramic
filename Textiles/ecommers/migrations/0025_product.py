# Generated by Django 5.0.7 on 2024-09-18 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommers', '0024_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/images/')),
            ],
        ),
    ]