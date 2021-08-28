from django.contrib import admin

from .models import Comments


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active', 'user']
    list_editable = ['active']
    # readonly_fields = ['id_for','type']
