# Generated by Django 2.2.6 on 2020-01-07 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_auto_20200107_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(verbose_name='Ngay sinh'),
        ),
    ]