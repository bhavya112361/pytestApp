# Generated by Django 4.1.5 on 2023-01-29 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_client_projectlist_client_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Project_Users',
        ),
    ]
