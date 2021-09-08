from django.contrib import admin

from .models import Suppliers, Customers


@admin.register(Suppliers)
class SupplierAdmin(admin.ModelAdmin):
    exclude = ['is_superuser', ]


@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    exclude = ['is_superuser', ]
