# Generated by Django 3.2.6 on 2021-09-14 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0004_alter_devicemodel_name'),
        ('orders', '0008_auto_20210902_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='device_type',
        ),
        migrations.AlterField(
            model_name='order',
            name='device_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='devices.devicemodel', verbose_name='Модель/Устройство'),
        ),
    ]
