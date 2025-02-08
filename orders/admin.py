from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('requester_name', 'product_type', 'quantity', 'date')
    # سایر تنظیمات...

admin.site.register(Order, OrderAdmin)

