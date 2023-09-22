from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from clients.forms import ClientsCreateForm
from clients.models import Clients


# Create your views here.

def index(request):
    return render(request, 'clients/main.html')


class ClientsListView(ListView):
    model = Clients


class ClientsCreateView(CreateView):
    model = Clients
    form_class = ClientsCreateForm
    success_url = reverse_lazy('clients:clients_list')


class ClientsUpdateView(UpdateView):
    model = Clients
    form_class = ClientsCreateForm
    success_url = reverse_lazy('clients:clients_list')


class ClientsDetailView(DetailView):
    model = Clients
    form_class = ClientsCreateForm
    success_url = reverse_lazy('clients:clients_list')


class ClientsDeleteView(DeleteView):
    model = Clients
    success_url = reverse_lazy('clients:clients_list')
