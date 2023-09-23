from django.db import models

NULLABLE = {'blank': True, 'null': True}

from newsletter.models import MessageSettings


# Create your models here.
class Logs(models.Model):
    newsletter = models.ForeignKey(MessageSettings, on_delete=models.SET_NULL,
                                   verbose_name='рассылка', **NULLABLE)
    time = models.DateTimeField(auto_now_add=True, verbose_name="время попытки")
    status = models.BooleanField(default=False, verbose_name='статус попытки', **NULLABLE)
    answer = models.TextField(verbose_name="ответ сервиса", **NULLABLE)

    def __str__(self):
        return f"logs:status {self.status}, newsletter {self.newsletter} "

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
