# Generated by Django 2.2.6 on 2020-01-07 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='IdentityS',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
