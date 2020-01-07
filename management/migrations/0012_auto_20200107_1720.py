# Generated by Django 2.2.6 on 2020-01-07 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0011_auto_20200107_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='edit',
            field=models.ImageField(default='edit.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('ON', 'Đang học'), ('OFF', 'Thôi học')], default='ON', max_length=5, verbose_name='Trạng thái'),
        ),
    ]
