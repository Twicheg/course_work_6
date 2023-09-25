from django.urls import path
from django.views.decorators.cache import cache_page

from newsletter.views import SettingsListView, SettingsCreateView, SettingsUpdateView, SettingsDeleteView, \
    SettingsDetailView, MessageCreateView, MessageListView, MessageDeleteView, MessageDetailView, MessageUpdateView
from newsletter.apps import NewsletterConfig

app_name = NewsletterConfig.name

urlpatterns = [
    path('list/', cache_page(60)(SettingsListView.as_view()), name='list'),
    path('create/', SettingsCreateView.as_view(), name='create'),
    path('update/<int:pk>/', SettingsUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', SettingsDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', SettingsDetailView.as_view(), name='detail'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/list/', cache_page(60)(MessageListView.as_view()), name='message_list'),
    path('message/delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),
    path('message/detail/<int:pk>', MessageDetailView.as_view(), name='message_detail'),
    path('message/update/<int:pk>', MessageUpdateView.as_view(), name='message_update'),

]
