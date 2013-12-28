'''
This is the entry point for the AI part of the project. Execute this script with
manage.py aiplanner event_id
the handle function is the entry point, call whatever needed there.
If more files are added and are not exposed as commands (class files for example)
name them with an underscore first for example _csp.py to avoid beeing registered
as commands
'''

from django.core.management.base import BaseCommand, CommandError
from events.models import *
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

        #self.stdout.write('Successfully loaded event "%s"' % event)

        # loading all activities
        activities = Activity.objects.all().filter(event=event)
        
        # loading all days
        days = {}
        for activity in activities:
            days[activity] = Day.objects.all().filter(activity=activity)
        
        # loading all votes
        votes = {}
        for day in days:
            votes[day] = Vote.objects.all().filter(day=day)

        #now we have all activities with its days and votes loaded
        #code here

        # test with datetime
        '''
        testday = datetime(2013, 12, 28, 10, 0, 0, 0,days[activities[0]][0].day.tzinfo)

        day_set = set([testday])

        print testday
        print days[activities[0]][0].day in day_set
        '''

        # test for app_csp_formulation
        
        formulate_app_csp(activities,days,votes)