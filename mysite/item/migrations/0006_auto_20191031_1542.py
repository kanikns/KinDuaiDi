# Generated by Django 2.2.6 on 2019-10-31 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_auto_20191031_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='create_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='update_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
