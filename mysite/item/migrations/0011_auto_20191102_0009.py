# Generated by Django 2.2.6 on 2019-11-01 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0010_auto_20191101_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 2, 0, 9, 48, 732164), editable=False),
        ),
    ]