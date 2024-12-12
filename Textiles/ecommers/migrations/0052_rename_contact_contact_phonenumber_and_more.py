# Generated by Django 5.0.7 on 2024-10-05 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommers', '0051_contact_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contact',
            new_name='phonenumber',
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='category_images/'),
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='city',
            field=models.CharField(editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='state',
            field=models.CharField(editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='streetaddress',
            field=models.CharField(editable=False, max_length=50),
        ),
    ]