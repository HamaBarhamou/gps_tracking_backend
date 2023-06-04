# Generated by Django 4.2.1 on 2023-06-04 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_alter_user_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Administrateur'), ('manager', 'Gestionnaire'), ('employee', 'Employé'), ('driver', 'driver')], max_length=20),
        ),
    ]
