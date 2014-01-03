'''
This is the entry point for the AI part of the project. Execute this script with
manage.py aiplanner event_id
the handle function is the entry point, call whatever needed there.
If more files are added and are not exposed as commands (class files for example)
name them with an underscore first for example _csp.py to avoid beeing registered
as commands
'''

from django.core.management.base import BaseCommand, CommandError
from datetime import *
from app_csp import*

class Command(BaseCommand):
    args = '<event_id>'
    help = 'Executes de AI planner on an event'

    def handle(self, *args, **options):
        event_id = args[0]
        try:
            event = Event.objects.get(pk=int(event_id))
        except Event.DoesNotExist:
            raise CommandError('Event "%s" does not exist' % event_id)
        formulate_app_csp(event)