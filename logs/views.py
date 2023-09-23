from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from logs.models import Logs


# Create your views here.
class LogsListView(ListView):
    model = Logs

class LogsDetailView(DetailView):
    model = Logs


class LogsDeleteView(DeleteView):
    model = Logs
    success_url = reverse_lazy('logs:list')




