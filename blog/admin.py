from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'text_body', 'image', 'number_of_views', 'publication_date']
    list_filter = ['title', 'number_of_views']
    search_fields = ['title']
