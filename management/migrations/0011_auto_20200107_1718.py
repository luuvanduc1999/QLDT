# Generated by Django 2.2.6 on 2020-01-07 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_auto_20200107_1626'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Học Sinh', 'verbose_name_plural': 'Học Sinh'},
        ),
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('ON', 'Đang học'), ('OFF', 'Thôi học')], default='ON', max_length=5),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(verbose_name='Ngày sinh'),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='', verbose_name='Ảnh thẻ'),
        ),
    ]