from django.contrib import admin
from .models import Order
from django.urls import reverse

#admin.site.register(Order)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'date_order', 'device_name', 'customer', 'comment')
    fields = [('order_date', 'status'), 'customer', ('device_type', 'device_model'), ('appearance', 'equipment'),
              ('defect', 'inspection'), ('employee', 'comment'), 'cost']
    list_display_links = ('id', 'device_name',)
    list_filter = ('order_date', 'status', 'device_type', 'employee')
    list_editable = ('status', 'comment')
    search_fields = ('id', 'customer__name', 'customer__phone')

    def device_name(self,obj):
        return f'{obj.device_type} {obj.device_model}'

    def date_order(self, obj):
        return obj.order_date.strftime("%d.%m.%Y")

    def view_on_site(self, obj):
        url = reverse('order-detail', kwargs={'pk': obj.pk})

        return url