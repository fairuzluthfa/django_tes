# Generated by Django 5.1.5 on 2025-02-17 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vision_app', '0002_alter_unit_model_upt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit_model',
            name='UPT',
        ),
    ]
