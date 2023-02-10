from django.contrib import admin 

from .models import Site, News


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url', 'created_at']
    fields = ['name', 'url', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'sentiment', 'site', 'created_at']
    fields = ['title', 'description', 'sentiment', 'site', 
              'url', 'image_url', 'created_at', 'updated_at']
    readonly_fields = ['url', 'image_url', 'created_at', 'updated_at']
