# Generated by Django 5.1.5 on 2025-02-05 07:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_musician_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.musician'),
        ),
    ]
