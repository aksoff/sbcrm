from django.contrib import admin
from .models import Firm, Office, Position, Employee, Customer

admin.site.register(Firm)
admin.site.register(Office)
admin.site.register(Position)
admin.site.register(Employee)
# admin.site.register(Customer)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('name', 'phone')
