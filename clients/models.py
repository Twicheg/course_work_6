from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Clients(models.Model):
    email = models.CharField(max_length=150, verbose_name='емейл')
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='имя')
    surname = models.CharField(max_length=100, verbose_name='имя')
    comments = models.TextField(verbose_name='комментарии')

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'