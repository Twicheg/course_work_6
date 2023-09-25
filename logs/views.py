from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from logs.models import Logs


class LogsListView(LoginRequiredMixin, ListView):
    model = Logs


class LogsDetailView(LoginRequiredMixin, DetailView):
    model = Logs


class LogsDeleteView(LoginRequiredMixin, DeleteView):
    model = Logs
    success_url = reverse_lazy('logs:list')
