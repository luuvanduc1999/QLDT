# Generated by Django 2.2.6 on 2020-01-13 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0019_auto_20200112_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='', verbose_name='Ảnh thẻ'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='', verbose_name='Ảnh thẻ'),
        ),
    ]
