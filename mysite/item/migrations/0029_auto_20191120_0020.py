# Generated by Django 2.2.7 on 2019-11-19 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0028_item_amount_forreserve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='amount_forreserve',
            field=models.IntegerField(default=0),
        ),
    ]
