from django.contrib import admin
from .models import Order
from django.urls import reverse
from services.sms.smsc_api import *


@admin.action(description='Пометить как: Выдан')
def make_issued(modeladmin, request, queryset):
    queryset.update(status=5)




@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'date_order', 'device_name', 'customer', 'cost', 'notified')
    fields = [('order_date', 'status'), ('customer', 'notified'), ('device_model', 'serial'), ('appearance', 'equipment'),
              ('defect', 'inspection'), ('employee', 'comment'), ('cost', 'zip_cost'), ('notes', )]
    list_display_links = ('id', 'device_name',)
    list_filter = ('order_date', 'status', 'employee', 'device_model__type__name')
    list_editable = ('status', 'cost', 'notified')
    search_fields = ('id', 'customer__name', 'customer__phone')
    autocomplete_fields = ('device_model', 'customer')
    actions = [make_issued, 'send_sms_status']

    @admin.action(description="action")
    def make_published(self, request, queryset):
        queryset.update(status='p')

    def device_name(self, obj):
        return f'{obj.device_model} {obj.defect}'

    device_name.short_description = "Устройство/Неисправность"

    def date_order(self, obj):
        return obj.order_date.strftime("%d.%m.%Y")

    date_order.short_description = "Дата"

    def view_on_site(self, obj):
        url = reverse('order-detail', kwargs={'pk': obj.pk})
        return url

    def print_order(self, obj):
        url = reverse('order-print', kwargs={'pk': obj.pk})
        return url

    @admin.action(description='Отправить СМС')
    def send_sms_status(self, request, queryset):
        smsc = SMSC()
        r = smsc.send_sms("+79276252962", "test message4 FROM django")
        queryset.update(notified=True)
        self.message_user(request, "SMS was send succesful!!")


