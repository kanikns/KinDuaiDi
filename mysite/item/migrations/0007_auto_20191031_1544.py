# Generated by Django 2.2.6 on 2019-10-31 08:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_auto_20191031_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 31, 15, 44, 51, 182033)),
        ),
    ]