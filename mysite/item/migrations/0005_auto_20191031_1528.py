# Generated by Django 2.2.6 on 2019-10-31 08:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_item_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='update_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='create_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
