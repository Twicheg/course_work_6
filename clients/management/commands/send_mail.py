from django.core.management import BaseCommand
from services.message import send_message



class Command(BaseCommand):
    def handle(self, *args, **options):
        send_message()