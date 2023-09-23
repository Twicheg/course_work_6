# from django.urls import path
# from django.views.decorators.cache import cache_page
#
# from clients.apps import ClientsConfig
# from clients.views import index, ClientsListView, ClientsCreateView, ClientsUpdateView, ClientsDetailView, \
#     ClientsDeleteView
#
# app_name = ClientsConfig.name
#
# urlpatterns = [
#     path('', index, name='main'),
#     path('clients/list/', ClientsListView.as_view(), name='clients_list'),
#     path('clients/create/', ClientsCreateView.as_view(), name='client_create'),
#     path('clients/update/<int:pk>', ClientsUpdateView.as_view(), name='client_update'),
#     path('client/<int:pk>', ClientsDetailView.as_view(), name='client_detail'),
#     path('client/delete/<int:pk>', ClientsDeleteView.as_view(), name='client_delete'),
# ]
