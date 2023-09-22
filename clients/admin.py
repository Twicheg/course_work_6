from django.contrib import admin

from clients.models import Clients
from logs.models import Logs
from newsletter.models import NewsletterSettings, Message


# Register your models here.
@admin.register(Clients)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'surname', 'comments']
    list_filter = ['last_name']
    search_fields = ['email']


@admin.register(NewsletterSettings)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['client', 'start_time', 'newsletter_time', 'periodicity', 'status']
    list_filter = ['status']


@admin.register(Message)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['newsletter', 'message_theme']


@admin.register(Logs)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['newsletter', 'status']