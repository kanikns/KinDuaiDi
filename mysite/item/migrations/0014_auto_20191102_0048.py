# Generated by Django 2.2.6 on 2019-11-01 17:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0013_auto_20191102_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 2, 0, 48, 25, 118980), editable=False),
        ),
    ]
