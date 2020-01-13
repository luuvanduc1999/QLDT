# Generated by Django 2.2.6 on 2020-01-13 10:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20200113_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500, verbose_name='Tiêu đề')),
                ('note', models.CharField(help_text='VD: Học kỳ, ...', max_length=500, verbose_name='Ghi chú')),
                ('caption', models.TextField(blank=True, help_text='VD: Nhắc nhở, Thông tin thêm...', verbose_name='Nội dung')),
                ('thumb', models.ImageField(help_text='Hiển thị trên trang chủ', null=True, upload_to='', verbose_name='Thumb')),
                ('submission_date', models.DateTimeField(default=datetime.datetime(2020, 1, 13, 17, 4, 37, 132386), editable=False)),
                ('edit', models.ImageField(blank=True, default='edit.png', null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Thông báo',
                'verbose_name_plural': 'Thông báo',
            },
        ),
        migrations.AlterField(
            model_name='scheduleweek',
            name='submission_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 13, 17, 4, 37, 131513), editable=False),
        ),
    ]