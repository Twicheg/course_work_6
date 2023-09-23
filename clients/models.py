from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Clients(models.Model):
    email = models.CharField(max_length=150, verbose_name='емейл')
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    surname = models.CharField(max_length=100, verbose_name='отчество')
    comments = models.TextField(verbose_name='комментарии')

    def __str__(self):
        return f'{self.email},{self.last_name}'
    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'