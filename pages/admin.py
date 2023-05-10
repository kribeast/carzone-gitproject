from django.contrib import admin
from .models import Teams
from django.utils.html import format_html

# Register your models here.

class TeamsAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(f'<img src="{object.photo.url}" width="40" style="border-radius:50px"  />')
    
    thumbnail.short_description = 'Image'

    list_display=['id','thumbnail','first_name','designation','created_at']
    list_display_links = ['id','thumbnail','first_name']
    search_fields = ['first_name','last_name','designation']
    list_filter = ['designation']

admin.site.register(Teams, TeamsAdmin)