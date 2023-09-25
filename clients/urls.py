from django.urls import path
from django.views.decorators.cache import cache_page

from clients.apps import ClientsConfig
from clients.views import index, ClientsListView, ClientsCreateView, ClientsUpdateView, ClientsDetailView, \
    ClientsDeleteView, NewTemplateView

app_name = ClientsConfig.name

urlpatterns = [
    path('', index, name='main'),
    path('clients/list/', cache_page(30)(ClientsListView.as_view()), name='clients_list'),
    path('clients/create/', ClientsCreateView.as_view(), name='client_create'),
    path('clients/update/<int:pk>', ClientsUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>', ClientsDetailView.as_view(), name='client_detail'),
    path('client/delete/<int:pk>', ClientsDeleteView.as_view(), name='client_delete'),
    path('create/newsletter/', cache_page(60)(NewTemplateView.as_view()), name='client_new'),

]
