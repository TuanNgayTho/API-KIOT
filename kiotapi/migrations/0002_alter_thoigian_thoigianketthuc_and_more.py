# Generated by Django 4.0.4 on 2022-06-11 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiotapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thoigian',
            name='THoiGianKetThuc',
            field=models.DateField(max_length=255),
        ),
        migrations.AlterField(
            model_name='thoigian',
            name='ThoiGianBatDau',
            field=models.DateField(max_length=255),
        ),
    ]
