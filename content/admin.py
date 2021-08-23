from django.contrib import admin
from .models import Category, CategoryType, Products, Tags, ProductsGalleries


# @admin.register(Category)
class CategoryInLine(admin.StackedInline):
    model = Category


@admin.register(CategoryType)
class CategoryTypeAdmin(admin.ModelAdmin):
    inlines = [CategoryInLine, ]
    list_display = ['__str__', 'have_subcategory']


@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active']
    list_editable = ['active']
    sortable_by = ['created_by', 'active']


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'inventory', 'created_by', 'active']
    list_editable = ['active']
    sortable_by = ['inventory', 'created_by', 'active']


@admin.register(ProductsGalleries)
class ProductsGalleriesAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'product', 'active']
    list_editable = ['active']
