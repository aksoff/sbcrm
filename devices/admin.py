from django.contrib import admin
from .models import DeviceType, Brand, DeviceModel

# admin.site.register(DeviceModel)
admin.site.register(DeviceType)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    fields = ('name',)
    list_editable = ('name',)
    search_fields = ('name',)


@admin.register(DeviceModel)
class DeviceModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'brand', 'name')
    fields = ('type', 'brand', 'name')
    list_editable = ('type', 'brand')
    search_fields = ('type__name', 'name', 'brand__name')
    autocomplete_fields = ('brand',)

