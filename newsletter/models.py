from django.db import models

from clients.models import Clients

NULLABLE = {'blank': True, 'null': True}


class NewsletterSettings(models.Model):
    period_daily = 'daily'
    period_weekly = 'weekly'
    period_monthly = 'monthly'

    period = (
        (period_daily, 'Ежедневно'),
        (period_weekly, 'Раз в неделю'),
        (period_monthly, 'Раз в месяц'),
    )

    status_created = 'created'
    status_started = 'started'
    status_done = 'done'

    status = (
        (status_created, 'Создана'),
        (status_started, 'Запущены'),
        (status_done, 'Завершена'),
    )

    client = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name='Клиент')
    start_time = models.TimeField(verbose_name="назначенное время расслыки")
    newsletter_time = models.DateTimeField(auto_now_add=True, verbose_name='время рассылки')
    periodicity = models.CharField(max_length=20, choices=period, default=period_daily, verbose_name='переодичность')
    status = models.CharField(max_length=20, choices=status, default=status_created, verbose_name='статус')

    def __str__(self):
        return f'{self.newsletter_time, self.periodicity, self.status}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Message(models.Model):
    newsletter = models.ForeignKey(NewsletterSettings, on_delete=models.CASCADE, verbose_name='рассылка')
    message_body = models.TextField(verbose_name='сообщение')
    message_theme = models.CharField(max_length=150, verbose_name='тема сообщения')

    def __str__(self):
        return f'{self.message_theme, self.message_body,}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'