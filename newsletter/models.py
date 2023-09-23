from django.db import models

NULLABLE = {'blank': True, 'null': True}


class MessageSettings(models.Model):
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

    start_time = models.TimeField(verbose_name="назначенное время старта расслыки", **NULLABLE)
    newsletter_time = models.DateTimeField(auto_now_add=True, verbose_name='время рассылки', **NULLABLE)
    periodicity = models.CharField(max_length=20, choices=period, default=period_daily, verbose_name='переодичность')
    status = models.CharField(max_length=20, choices=status, default=status_created, verbose_name='статус')
    message_id = models.ForeignKey('Message', on_delete=models.CASCADE, verbose_name='message_id', **NULLABLE)

    def __str__(self):
        return f'{self.periodicity, self.status}'


class Message(models.Model):
    client = models.ForeignKey('clients.Clients', on_delete=models.CASCADE, verbose_name='Клиент', **NULLABLE)
    settings = models.ForeignKey('MessageSettings', on_delete=models.CASCADE, verbose_name='Настройка', **NULLABLE)
    message_body = models.TextField(verbose_name='сообщение')
    message_theme = models.CharField(max_length=150, verbose_name='тема сообщения')

    def __str__(self):
        return f'{self.message_theme, self.message_body}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
