# Generated by Django 5.1.5 on 2025-02-16 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iot_app', '0002_alter_sensordata_device'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensordata',
            old_name='device',
            new_name='devices',
        ),
    ]
