from django.contrib import admin

from newsletter.models import Message, MessageSettings


@admin.register(MessageSettings)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','start_time', 'day_to_send' , 'status']
   # list_filter = ['status']


@admin.register(Message)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','client', 'message_theme']
