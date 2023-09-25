from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from logs.models import Logs


class LogsListView(LoginRequiredMixin, ListView):
    model = Logs
    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return super().get_queryset()
        else:
            raise Http404


class LogsDetailView(LoginRequiredMixin, DetailView):
    model = Logs


class LogsDeleteView(LoginRequiredMixin, DeleteView):
    model = Logs
    success_url = reverse_lazy('logs:list')
