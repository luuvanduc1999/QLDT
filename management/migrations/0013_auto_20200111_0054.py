# Generated by Django 2.2.6 on 2020-01-10 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_auto_20200107_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='addr',
            field=models.TextField(default='', max_length=500, verbose_name='Địa chỉ thường trú'),
        ),
        migrations.AddField(
            model_name='student',
            name='datebegin',
            field=models.DateField(null=True, verbose_name='Ngày nhập học'),
        ),
        migrations.AddField(
            model_name='student',
            name='dobdad',
            field=models.DateField(null=True, verbose_name='Ngày sinh bố'),
        ),
        migrations.AddField(
            model_name='student',
            name='dobmom',
            field=models.DateField(null=True, verbose_name='Ngày sinh mẹ'),
        ),
        migrations.AddField(
            model_name='student',
            name='ethnic',
            field=models.CharField(max_length=100, null=True, verbose_name='Dân tộc'),
        ),
        migrations.AddField(
            model_name='student',
            name='hometown',
            field=models.CharField(max_length=200, null=True, verbose_name='Quê quán'),
        ),
        migrations.AddField(
            model_name='student',
            name='jobdad',
            field=models.CharField(max_length=200, null=True, verbose_name='Nghề nghiệp bố'),
        ),
        migrations.AddField(
            model_name='student',
            name='jobmom',
            field=models.CharField(max_length=200, null=True, verbose_name='Nghề nghiệp mẹ'),
        ),
        migrations.AddField(
            model_name='student',
            name='namedad',
            field=models.CharField(max_length=200, null=True, verbose_name='Họ tên bố'),
        ),
        migrations.AddField(
            model_name='student',
            name='namemom',
            field=models.CharField(max_length=200, null=True, verbose_name='Họ tên mẹ'),
        ),
        migrations.AddField(
            model_name='student',
            name='phonenum',
            field=models.CharField(max_length=20, null=True, verbose_name='Số điện thoại liên hệ'),
        ),
        migrations.AddField(
            model_name='student',
            name='religion',
            field=models.CharField(default='Không', max_length=100, verbose_name='Tôn giáo'),
        ),
        migrations.AlterField(
            model_name='student',
            name='Years',
            field=models.IntegerField(default=2019, verbose_name='Khóa học'),
        ),
    ]