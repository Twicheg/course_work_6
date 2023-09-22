import os, sys

from django.core.mail import send_mail


def send_message():
    send_mail(subject='Генерация пароля',
        message=f'{password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
                      )
