# Generated by Django 3.2.6 on 2021-09-14 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_alter_devicemodel_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicemodel',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='devices.devicetype', verbose_name='Тип устройства'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='type',
            field=models.ManyToManyField(help_text='Выберите типы устройств', related_name='brands', to='devices.DeviceType', verbose_name='Устройства'),
        ),
    ]