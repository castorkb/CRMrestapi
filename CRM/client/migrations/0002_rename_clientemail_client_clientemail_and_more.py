# Generated by Django 5.1.2 on 2024-10-28 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='ClientEmail',
            new_name='clientEmail',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='ClientName',
            new_name='clientName',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='ClientPhonenamber',
            new_name='clientPhonenamber',
        ),
    ]