# Generated by Django 2.2.1 on 2019-05-14 06:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190513_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 14, 15, 27, 10, 50710), verbose_name='date published'),
        ),
    ]
