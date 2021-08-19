from django.contrib import admin
from .models import Category, CategoryType, Products


# @admin.register(Category)
class CategoryInLine(admin.StackedInline):
    model = Category


@admin.register(CategoryType)
class CategoryTypeAdmin(admin.ModelAdmin):
    inlines = [CategoryInLine, ]
    list_display = ['__str__', 'have_subcategory']


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'inventory', 'created_by', 'active']
    list_editable = ['active']
    sortable_by = ['inventory', 'created_by', 'active']
