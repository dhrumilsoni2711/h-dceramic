# Generated by Django 5.1.2 on 2024-10-26 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommers', '0056_delete_billinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='u_email',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='id',
        ),
        migrations.AddField(
            model_name='cart',
            name='c_id',
            field=models.CharField(default='harsh', editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
    ]
