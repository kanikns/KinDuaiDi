# Generated by Django 2.2.6 on 2019-10-31 08:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0008_auto_20191031_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 31, 15, 58, 55, 879953), editable=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]