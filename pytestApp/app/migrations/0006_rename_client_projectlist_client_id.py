# Generated by Django 4.1.5 on 2023-01-29 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_projectlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectlist',
            old_name='client',
            new_name='client_id',
        ),
    ]