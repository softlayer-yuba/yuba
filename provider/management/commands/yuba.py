from django.core.management.base import BaseCommand

from provider.api import Provider

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print args
        print kwargs
        provider = Provider()
        print provider.create_instance()
