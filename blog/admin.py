from django.contrib import admin

# Register your models here.
from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created',
        'updated',
    )
    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )
    list_filter = (
        'status',
    )

admin.site.register(models.Post, PostAdmin)