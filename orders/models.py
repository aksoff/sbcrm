from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from devices.models import DeviceType
from django.urls import reverse
from datetime import datetime


class Order(models.Model):
    ORDER_STATUS = (
        (1, 'Диагностика'),
        (2, 'На согласовании'),
        (3, 'В ремонте'),
        (4, 'Готов'),
        (5, 'Выдан'),
        (6, 'Архив'),
        (7, 'Отказ от ремонта'),
        (8, 'Ожидает запчасти')
    )
    order_date = models.DateTimeField(default=datetime.now, verbose_name='Дата/Время')
    status = models.IntegerField(choices=ORDER_STATUS, default=1, verbose_name='Статус')
    customer = models.ForeignKey('directory.Customer', on_delete=models.CASCADE, verbose_name='Клиент')
    device_model = models.ForeignKey('devices.DeviceModel', on_delete=models.SET_NULL, null=True, verbose_name='Устройство/Модель')
    equipment = models.CharField(max_length=255, verbose_name='В комплекте', null=True, blank=True)
    defect = models.CharField(max_length=255, verbose_name='Неисправность')
    appearance = models.CharField(max_length=255, verbose_name='Внешний вид')
    inspection = models.CharField(max_length=255, verbose_name='Предварительный осмотр')
    employee = models.ForeignKey('directory.Employee', on_delete=models.SET_NULL, null=True, verbose_name='Исполнитель')
    comment = models.CharField(max_length=1024, verbose_name='Комментарий', default='', blank=True)
    cost = models.DecimalField(verbose_name='Стоимость', max_digits=10, decimal_places=2, default=300)
    zip_cost = models.DecimalField(verbose_name='Стоимость запчастей', max_digits=10, decimal_places=2, default=0)
    notified = models.BooleanField(verbose_name='Уведомлен', default=False)
    serial = models.CharField(max_length=25, verbose_name='Серийный номер', default='б/н')
    notes = RichTextUploadingField(verbose_name='Заметки', null=True, blank=True)
    # notes = models.TextField(max_length=1048, verbose_name='Заметки', null=True, blank=True)

    class Meta:
        verbose_name = 'Заявка на ремонт'
        verbose_name_plural = 'Заявки на ремонт'

    def __str__(self):
        return f'Заявка СБ-0{self.id} от {self.order_date}'

    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"pk": self.pk})