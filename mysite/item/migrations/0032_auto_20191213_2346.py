# Generated by Django 2.2.6 on 2019-12-13 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0031_auto_20191124_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
