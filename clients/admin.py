from django.contrib import admin

from clients.models import Clients
from logs.models import Logs
from newsletter.models import Message


# Register your models here.
@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'surname', 'comments']
    list_filter = ['last_name']
    search_fields = ['email']
