# Generated by Django 5.0.4 on 2024-04-30 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='year',
        ),
        migrations.AddField(
            model_name='car',
            name='production_date',
            field=models.DateField(default=datetime.datetime(2024, 4, 30, 11, 50, 58, 297208, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
