from django.contrib import admin
from django.utils.safestring import mark_safe
from blog.models import *



# admin.site.register
@admin.register(TechModel)
class TechAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'skill', 'activated', 'ordering')
    list_display_links = ('id', 'name',)
    list_editable = ('skill', 'activated', 'ordering')

    fieldsets = (
        ( None, { 'fields': (('skill', 'activated',), ('name', 'ordering'), ) }),
    )


@admin.register(BookmarkModel)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'clickable_url',)
    list_display_links = ('id', 'title',)

    def clickable_url(self, obj):
        return mark_safe(f'<a href="{obj.url}" target="_blank">{obj.url}</a>')

    clickable_url.short_description = 'URL'


