# Generated by Django 2.2.6 on 2020-01-13 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20200113_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduleweek',
            name='edit',
            field=models.ImageField(blank=True, default='edit.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='scheduleweek',
            name='submission_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 13, 14, 52, 4, 16703), editable=False),
        ),
    ]
