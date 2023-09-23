from django.contrib import admin

from logs.models import Logs


@admin.register(Logs)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['newsletter', 'time', 'status', 'answer']
    list_filter = ['time', 'newsletter']
