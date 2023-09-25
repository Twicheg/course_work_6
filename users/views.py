import random
import time

from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

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
    print(pk)
    for i in User.objects.all():
        print(i,i.verification)
        if i.verification == pk and i.email == User.objects.get(verification=pk).email:
            i.is_active = True
            i.save()
    return render(request, 'users/verification.html')


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
