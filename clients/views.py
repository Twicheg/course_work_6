import random

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView

from blog.models import Blog
from clients.forms import ClientsCreateForm
from clients.models import Clients
from newsletter.models import MessageSettings
from services.permissions import get_permissions
from users.models import User


# Create your views here.

def index(request):
    if request.method == "GET":
        get_permissions(request)
    list = [i for i in Blog.objects.all()]
    random.shuffle(list)
    context = {
        'count_of_newsletter': len([i for i in MessageSettings.objects.all()]),
        'active_news': len([i for i in MessageSettings.objects.filter(status='started')]),
        'uniq_clients': len({i.email for i in Clients.objects.all()}),
        'blog_list': list
    }

    return render(request, 'clients/main.html', context)


class ClientsListView(LoginRequiredMixin, ListView):
    model = Clients

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        else:
            queryset = queryset.filter(content_creator=self.request.user)
            return queryset


class ClientsCreateView(LoginRequiredMixin, CreateView):
    model = Clients
    form_class = ClientsCreateForm
    success_url = reverse_lazy('clients:clients_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.content_creator = self.request.user.email
        self.object.save()
        return super().form_valid(form)


class ClientsUpdateView(LoginRequiredMixin, UpdateView):
    model = Clients
    form_class = ClientsCreateForm
    success_url = reverse_lazy('clients:clients_list')

    def get_object(self, queryset=None):
        self.object = super().get_object()
        if self.object.content_creator != self.request.user.email:
            raise Http404
        return self.object

    def get_success_url(self):
        return reverse('clients:client_detail', args=[self.object.id])


class ClientsDetailView(LoginRequiredMixin, DetailView):
    model = Clients
    form_class = ClientsCreateForm
    success_url = reverse_lazy('clients:clients_list')

    def get_object(self, queryset=None):
        self.object = super().get_object()
        if not self.request.user.is_staff and self.object.content_creator != self.request.user.email:
            raise Http404
        return self.object


class ClientsDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'clients.delete_clients'
    model = Clients
    success_url = reverse_lazy('clients:clients_list')

    def get_object(self, queryset=None):
        self.object = super().get_object()
        if self.object.content_creator != self.request.user.email:
            raise Http404
        return self.object


class NewTemplateView(TemplateView):
    template_name = 'clients/create_newsletter.html'
