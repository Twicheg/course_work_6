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
    client = models.ForeignKey('clients.Clients', verbose_name='клиент', on_delete=models.CASCADE, **NULLABLE)
    start_time = models.DateTimeField(verbose_name="назначенное время старта расслыки", **NULLABLE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='время рассылки', **NULLABLE)
    periodicity = models.CharField(max_length=20, choices=period, default=period_daily, verbose_name='переодичность')
    status = models.CharField(max_length=20, choices=status, default=status_created, verbose_name='статус')
    message_counter = models.IntegerField(verbose_name='счетчик',default=0)
    day_to_send = models.IntegerField(default=7, verbose_name='Кол-во дней для отправки', **NULLABLE)
    message_id = models.ForeignKey('Message', on_delete=models.CASCADE, verbose_name='message_id', **NULLABLE)
    content_creator = models.CharField(max_length=50, verbose_name='создатель рассылки', **NULLABLE)
    def __str__(self):
        return f'{self.message_id, self.start_time, self.periodicity, self.status}'

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'


class Message(models.Model):
    client = models.ForeignKey('clients.Clients', on_delete=models.CASCADE, verbose_name='Клиент', **NULLABLE)
    settings = models.ForeignKey('MessageSettings', on_delete=models.CASCADE, verbose_name='Настройка', **NULLABLE)
    message_body = models.TextField(verbose_name='сообщение')
    message_theme = models.CharField(max_length=150, verbose_name='тема сообщения')
    content_creator = models.CharField(max_length=50, verbose_name='создатель текста', **NULLABLE)

    def __str__(self):
        return f'Тема:{self.message_theme} Сообщение:{self.message_body}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
