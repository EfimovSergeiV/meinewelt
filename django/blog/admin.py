from django.contrib import admin
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


admin.site.register(ArticleModel)


