# Generated by Django 4.0.4 on 2022-06-13 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiotapi', '0002_alter_thoigian_thoigianketthuc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thoigian',
            name='THoiGianKetThuc',
            field=models.DateTimeField(max_length=255),
        ),
        migrations.AlterField(
            model_name='thoigian',
            name='ThoiGianBatDau',
            field=models.DateTimeField(max_length=255),
        ),
    ]
