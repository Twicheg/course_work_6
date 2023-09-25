from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from clients.forms import ClientsCreateForm
from clients.models import Clients
from newsletter.models import MessageSettings


# Create your views here.

def index(request):
    return render(request, 'clients/main.html')


class ClientsListView(ListView):
    model = Clients


class ClientsCreateView(CreateView):
    model = Clients
    form_class = ClientsCreateForm
    success_url = reverse_lazy('clients:clients_list')

    def form_valid(self, form):
        self.object = form.save
        self.object.content_creator = self.request.user
        return super().form_valid(form)


class ClientsUpdateView(UpdateView):
    model = Clients
    form_class = ClientsCreateForm
    success_url = reverse_lazy('clients:clients_list')

    def get_success_url(self):
        return reverse('clients:client_detail', args=[self.object.id])


class ClientsDetailView(DetailView):
    model = Clients
    form_class = ClientsCreateForm
    success_url = reverse_lazy('clients:clients_list')


class ClientsDeleteView(DeleteView):
    model = Clients
    success_url = reverse_lazy('clients:clients_list')
