import random
import time

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from config import settings
from services.message import mail
from users.forms import UserForm, UserUpdateForm
from users.models import User


# Create your views here.
class LIView(LoginView):
    template_name = 'users/login.html'


class LOView(LogoutView):
    template_name = 'users/logout.html'


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        verification = random.randint(100000, 999999)
        new_user = form.save()
        mail(message=f'http://127.0.0.1:8000/users/verification/{verification}', title='Верификация',
             client=new_user.email)
        new_user.verification = verification
        new_user.save()
        return super().form_valid(form)


def verification(request, pk):
    for i in User.objects.all():
        if i.verification == pk and i.email == User.objects.get(verification=pk).email:
            i.is_active = True
            i.save()
    return render(request, 'users/verification.html')


@login_required
@permission_required('users.change_user')
def user_deactivate(request, pk):
    for i in User.objects.all():
        if i.id == pk:
            i.is_active = False
            i.save()
    return redirect(reverse('users:list'))


def user_activate(request, pk):
    for i in User.objects.all():
        if i.id == pk:
            i.is_active = True
            i.save()

    return redirect(reverse('users:list'))


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:update')
    form_class = UserUpdateForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data

    def get_object(self, queryset=None):
        return self.request.user


def genpass(request):
    password = str(random.randint(0, 999999))
    request.user.set_password(password)
    request.user.save()
    mail(password)
    send_mail(message=password, title='Генерация пароля', client=request.user.email)

    return redirect(reverse('users:login'))


class UserListView(ListView):
    model = User

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff or self.request.user.is_superuser:
            return queryset
        else:
            return Http404

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(**kwargs)

    def post(self, request):
        if self.request.method == 'POST':
            for i in User.objects.all():
                if i.email == self.request.POST.get('name'):
                    i.is_staff = True
                    i.save()
        return redirect(reverse('users:list'))

    template_name = 'users/users_list.html'


class UserDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'users.del_user'
    model = User
    template_name = 'users/users_confirm_delete.html'
    success_url = reverse_lazy('users:list')
