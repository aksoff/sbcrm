from django.db import models


class DeviceType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Тип устройства')

    class Meta:
        verbose_name = 'Тип Устройства'
        verbose_name_plural = 'Типы устройств'

    def __str__(self):
        return f'{self.name}'


class Brand(models.Model):
    objects = None
    name = models.CharField(max_length=255, verbose_name='Производитель')
    type = models.ManyToManyField(DeviceType, verbose_name='Устройства', related_name='brands', help_text='Выберите типы устройств')

    class Meta:
        verbose_name = 'Производитель/Бренд'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return f'{self.name}'


class DeviceModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Модель')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Бренд')

    class Meta:
        verbose_name = 'Модель устройства'
        verbose_name_plural = 'Модели устройств'

    def __str__(self):
        return f'{self.brand.name} {self.name}'
