from django.contrib.auth.models import AbstractUser
from django.db import models

from clients.models import NULLABLE


# class User(AbstractUser):
#     username = None
#
#     email = models.EmailField(unique=True, verbose_name='email')
#     avatar = models.ImageField(upload_to='users', verbose_name='аватар', **NULLABLE)
#     phone_number = models.CharField(max_length=50, verbose_name='номер телефона', **NULLABLE)
#     # is_active = models.BooleanField(default=False, verbose_name='активность')
#     # is_staff = models.BooleanField(default=False, verbose_name='модератор')
#     country = models.CharField(max_length=20, verbose_name='страна')
#     verification = models.IntegerField(verbose_name='ключ верификации', **NULLABLE)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
