from django.contrib import admin
from .models import Brands, Category, Products, Tags, ProductsGalleries


@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    model = Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'parent']


@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active']
    list_editable = ['active']
    sortable_by = ['created_by', 'active']


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'inventory', 'supplier', 'active']
    list_editable = ['active']
    sortable_by = ['inventory', 'supplier', 'active']
    exclude = []

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return self.exclude
        else:
            return self.exclude + ['active']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(supplier=request.user)


@admin.register(ProductsGalleries)
class ProductsGalleriesAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'product', 'active']
    list_editable = ['active']
