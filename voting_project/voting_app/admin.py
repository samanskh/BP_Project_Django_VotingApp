# voting_app/admin.py

from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import Movie, Series

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_cover_image', 'points')

    def display_cover_image(self, obj):
        return mark_safe('<img src="{}" width="50" height="50" />'.format(obj.cover_image.url))
    display_cover_image.short_description = 'Cover Image'

class SeriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_cover_image', 'points')

    def display_cover_image(self, obj):
        return mark_safe('<img src="{}" width="50" height="50" />'.format(obj.cover_image.url))
    display_cover_image.short_description = 'Cover Image'

admin.site.register(Movie, MovieAdmin)
admin.site.register(Series, SeriesAdmin)



