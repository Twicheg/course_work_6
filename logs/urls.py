from django.urls import path
from django.views.decorators.cache import cache_page

from logs.views import LogsListView, LogsDetailView, LogsDeleteView
from logs.apps import LogsConfig

app_name = LogsConfig.name

urlpatterns = [
    path('list/', LogsListView.as_view(), name='list'),
    path('detail/<int:pk>/', LogsDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', LogsDeleteView.as_view(), name='delete'),

]
