# Generated by Django 5.0.7 on 2024-08-12 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommers', '0008_delete_adminlogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(max_length=20, unique=True)),
                ('a_password', models.CharField(max_length=8)),
            ],
        ),
    ]