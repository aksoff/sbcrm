from django.contrib import admin
from .models import DeviceType, Brand, DeviceModel

# admin.site.register(DeviceModel)
admin.site.register(DeviceType)
admin.site.register(Brand)


@admin.register(DeviceModel)
class DeviceModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'brand', 'name')
    fields = ('type', 'brand', 'name')
    # search_fields = ("name", "brand")

