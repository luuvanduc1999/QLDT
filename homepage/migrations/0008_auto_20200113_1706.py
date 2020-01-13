# Generated by Django 2.2.6 on 2020-01-13 10:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20200113_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='file',
            field=models.FileField(blank=True, help_text='Văn bản', null=True, upload_to='', verbose_name='File đính kèm'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='submission_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 13, 17, 6, 42, 53013), editable=False),
        ),
        migrations.AlterField(
            model_name='scheduleweek',
            name='submission_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 13, 17, 6, 42, 52298), editable=False),
        ),
    ]