# Generated by Django 2.2.6 on 2019-12-13 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0004_auto_20191127_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='status',
            field=models.CharField(blank=True, choices=[('01', 'อยู่ในตะกร้า'), ('02', 'รออนุมัติ'), ('03', 'ยืนยันการยืม'), ('05', 'ยกเลิก')], max_length=2, null=True),
        ),
    ]