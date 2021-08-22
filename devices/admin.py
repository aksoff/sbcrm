from django.contrib import admin
from .models import DeviceType, Brand, DeviceModel

admin.site.register(DeviceModel)
admin.site.register(DeviceType)
admin.site.register(Brand)
