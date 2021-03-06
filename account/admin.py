from django.contrib import admin

from .models import Suppliers, Customers, Subscribers, Addresses


@admin.register(Suppliers)
class SupplierAdmin(admin.ModelAdmin):
    exclude = ['is_superuser', ]


@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    exclude = ['is_superuser', ]


@admin.register(Subscribers)
class SubscribersAdmin(admin.ModelAdmin):
    list_display = ["__str__", "active"]


@admin.register(Addresses)
class SubscribersAdmin(admin.ModelAdmin):
    pass
