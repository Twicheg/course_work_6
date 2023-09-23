import os, sys
import datetime
from django.conf import settings
from django.core.mail import send_mail

from logs.models import Logs
from newsletter.models import MessageSettings


def mail(message, title, client):
    return send_mail(subject=title,
                     message=message,
                     from_email=settings.EMAIL_HOST_USER,
                     recipient_list=[client]
                     )


def send_message():
    # print('asdasd')
    timenow = datetime.datetime.today().replace(microsecond=0)
    print(f'{datetime.datetime.today()}, crontab work')
    for obj in MessageSettings.objects.all():

        if obj.start_time is not None:
            start_time = obj.start_time.replace(tzinfo=None)
        else:
            start_time = obj.created_time.replace(tzinfo=None)

        if (start_time - timenow).days > obj.day_to_send:
            obj.status = 'done'
            print(f'{datetime.datetime.today()}, object {obj.client.email} status -> {obj.status}')

        if obj.status != 'done':
            if (timenow - start_time).seconds > 0 and obj.status == 'created':
                obj.status = 'started'
                obj.message_counter += 1
                print(f'{datetime.datetime.today()}, object {obj.client.email} status -> {obj.status}')
                error = mail(obj.message_id.message_body, obj.message_id.message_theme, obj.client.email)
                if error > 0:
                    Logs.objects.create(newsletter=MessageSettings.objects.get(pk=obj.pk), status=True, answer=error)
                else:
                    Logs.objects.create(newsletter=MessageSettings.objects.get(pk=obj.pk), status=False, answer=error)

            if obj.periodicity == 'daily' and (timenow - start_time).days > obj.message_counter and obj.status == 'started':
                print(f'{datetime.datetime.today()}, daily work')
                obj.message_counter += 1
                error = mail(obj.message_id.message_body, obj.message_id.message_theme, obj.client.email)
                if error > 0:
                    Logs.objects.create(newsletter=MessageSettings.objects.get(pk=obj.pk), status=True, answer=error)
                else:
                    Logs.objects.create(newsletter=MessageSettings.objects.get(pk=obj.pk), status=False, answer=error)

            elif obj.periodicity == 'weekly' and obj.status == 'started' and (timenow - start_time).days / 7 > obj.message_counter:
                print(f'{datetime.datetime.today()}, weekly work')
                obj.message_counter += 1
                error = mail(obj.message_id.message_body, obj.message_id.message_theme, obj.client.email)
                if error > 0:
                    Logs.objects.create(newsletter=MessageSettings.objects.get(pk=obj.pk), status=True, answer=error)
                else:
                    Logs.objects.create(newsletter=MessageSettings.objects.get(pk=obj.pk), status=False, answer=error)

            elif obj.periodicity == 'monthly' and obj.status == 'started' and (timenow - start_time).days / 30 > obj.message_counter:
                print(f'{datetime.datetime.today()}, monthly work')
                error = mail(obj.message_id.message_body, obj.message_id.message_theme, obj.client.email)
                if error > 0:
                    Logs.objects.create(newsletter=MessageSettings.objects.get(pk=obj.pk), status=True, answer=error)
                else:
                    Logs.objects.create(newsletter=MessageSettings.objects.get(pk=obj.pk), status=False, answer=error)
            obj.save()

