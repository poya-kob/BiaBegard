from django.contrib import admin

from .models import BlogCategory, Blog, Comments

admin.site.register(Blog)
admin.site.register(BlogCategory)
admin.site.register(Comments)
