# Generated by Django 2.2.6 on 2020-01-10 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0015_auto_20200111_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='level',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Trình độ cấp bậc'),
        ),
    ]
