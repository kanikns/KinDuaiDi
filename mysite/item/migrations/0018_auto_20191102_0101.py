# Generated by Django 2.2.6 on 2019-11-01 18:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0017_auto_20191102_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 2, 1, 1, 58, 577539), editable=False),
        ),
    ]
