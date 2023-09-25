from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from services.message import send_message
from clients.models import Clients
from newsletter.forms import NewsletterCreateForm, MessageCreateForm
from newsletter.models import MessageSettings, Message


# Create your views here.
class SettingsListView(LoginRequiredMixin, ListView):
    model = MessageSettings
    template_name = 'newsletter/newsletter_list.html'

    def post(self, request):
        if self.request.method == 'POST':
            for i in MessageSettings.objects.all():
                if i.id == int(self.request.POST.get('pk')):
                    i.status = 'done'
                    i.save()
        return redirect(reverse('newsletter:list'))

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        else:
            queryset = queryset.filter(content_creator=self.request.user.email)
            return queryset


class SettingsCreateView(LoginRequiredMixin, CreateView):
    model = MessageSettings
    template_name = 'newsletter/newsletter_form.html'
    form_class = NewsletterCreateForm
    success_url = reverse_lazy('clients:clients_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.content_creator = self.request.user.email
        self.object.save()
        return super().form_valid(form)


class SettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = MessageSettings
    template_name = 'newsletter/newsletter_form.html'
    form_class = NewsletterCreateForm
    success_url = reverse_lazy('newsletter:list')

    def get_object(self, queryset=None):
        self.object = super().get_object()
        if self.request.user.is_superuser:
            return self.object
        if self.object.content_creator != self.request.user.email:
            raise Http404
        return self.object


class SettingsDetailView(LoginRequiredMixin, DetailView):
    model = MessageSettings
    template_name = 'newsletter/newsletter_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object()
        if self.request.user.is_staff:
            return self.object
        if self.object.content_creator != self.request.user.email:
            raise Http404
        return self.object


class SettingsDeleteView(LoginRequiredMixin, DeleteView):
    model = MessageSettings
    template_name = 'newsletter/newsletter_confirm_delete.html'
    success_url = reverse_lazy('clients:main')

    def get_object(self, queryset=None):
        self.object = super().get_object()
        if self.request.user.is_superuser:
            return self.object
        if self.object.content_creator != self.request.user.email:
            raise Http404
        return self.object


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageCreateForm
    template_name = 'newsletter/message_form.html'
    success_url = reverse_lazy('newsletter:message_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.content_creator = self.request.user.email
        self.object.save()
        return super().form_valid(form)


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'newsletter/message_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        else:
            queryset = queryset.filter(content_creator=self.request.user)
            return queryset


class MessageDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'newsletter.def_message'
    model = Message
    template_name = 'newsletter/message_confirm_delete.html'
    success_url = reverse_lazy('newsletter:message_list')

    def get_object(self, queryset=None):
        self.object = super().get_object()
        if self.object.content_creator != self.request.user.email:
            raise Http404
        return self.object

    # def get_success_url(self):
    #     return reverse('clients:client_detail', args=[self.object.client_id])


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'newsletter/message_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object()
        if not self.request.user.is_staff and self.object.content_creator != self.request.user.email:
            raise Http404
        return self.object


class MessageUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'newsletter.change_message'
    model = Message
    template_name = 'newsletter/message_form.html'
    form_class = MessageCreateForm

    def get_object(self, queryset=None):
        self.object = super().get_object()
        if self.object.content_creator != self.request.user.email:
            raise Http404
        return self.object

    def get_success_url(self):
        return reverse('newsletter:message_detail', args=[self.object.id])
