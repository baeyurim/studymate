# Generated by Django 2.2.1 on 2019-05-14 06:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190514_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 14, 15, 27, 34, 431536), verbose_name='date published'),
        ),
    ]
