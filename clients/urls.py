from django.urls import path
from django.views.decorators.cache import cache_page

from clients.apps import ClientsConfig
from clients.views import index

app_name = ClientsConfig.name

urlpatterns = [
    path('', index, name='main'),
]