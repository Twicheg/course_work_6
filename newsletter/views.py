from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from services.message import send_message
from clients.models import Clients
from newsletter.forms import NewsletterCreateForm, MessageCreateForm
from newsletter.models import MessageSettings, Message


# Create your views here.
class SettingsListView(ListView):
    model = MessageSettings
    template_name = 'newsletter/newsletter_list.html'


class SettingsCreateView(CreateView):
    model = MessageSettings
    template_name = 'newsletter/newsletter_form.html'
    form_class = NewsletterCreateForm
    success_url = reverse_lazy('clients:clients_list')

    def form_valid(self, form):
        self.object = form.save
        self.object.content_creator = self.request.user
        return super().form_valid(form)


class SettingsUpdateView(UpdateView):
    model = MessageSettings
    template_name = 'newsletter/newsletter_form.html'
    form_class = NewsletterCreateForm
    success_url = reverse_lazy('clients:clients_list')


class SettingsDetailView(DetailView):
    model = MessageSettings
    template_name = 'newsletter/newsletter_detail.html'


class SettingsDeleteView(DeleteView):
    model = MessageSettings
    template_name = 'newsletter/newsletter_confirm_delete.html'
    success_url = reverse_lazy('clients:main')


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageCreateForm
    template_name = 'newsletter/message_form.html'
    success_url = reverse_lazy('clients:list')

    def form_valid(self, form):
        self.object = form.save
        self.object.content_creator = self.request.user
        return super().form_valid(form)



class MessageListView(ListView):
    model = Message
    template_name = 'newsletter/message_list.html'


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'newsletter/message_confirm_delete.html'

    def get_success_url(self):
        return reverse('clients:client_detail', args=[self.object.client_id])


class MessageDetailView(DetailView):
    model = Message
    template_name = 'newsletter/message_detail.html'


class MessageUpdateView(UpdateView):
    model = Message
    template_name = 'newsletter/message_form.html'
    form_class = MessageCreateForm

    def get_success_url(self):
        return reverse('newsletter:message_detail', args=[self.object.id])
