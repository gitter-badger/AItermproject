from django.shortcuts import redirect
from django.views.generic import ListView,DetailView
from events.models import *
from events.forms import *
from django.core import management


class IndexView(ListView):
    template_name = 'events/index.html'
    context_object_name = 'all_event_list'
    model = Event

class EventDetail(DetailView):
    pk_url_kwarg = 'pk_event' #I find more clear to use this name than only pk
    model = Event
    template_name = 'events/detail.html'

class EventCSPResultDetail(DetailView):
    pk_url_kwarg = 'pk_event' #I find more clear to use this name than only pk
    model = Event
    template_name = 'events/CSPresult.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EventCSPResultDetail, self).get_context_data(**kwargs)
        #solve the event
        #management.call_command('flush', verbosity=0, interactive=False)
        #context['TODO'] = ""
        return context

class ActivityDetailView(DetailView):
    model = Activity
    template_name = 'activities/detail.html'
    pk_url_kwarg = 'pk_activity' #I find more clear to use this name than only pk

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ActivityDetailView, self).get_context_data(**kwargs)
        #query for all days in the activity
        daylist = Day.objects.filter(activity=self.object.id)
        fields = []
        for day in daylist:
            fields.append({'name': str(day.id), 'label': day.dateAndTime })
        context['voteform'] = MultiVoteForm(dynamic_fields=fields)
        return context

    def post(self, request, *args, **kwargs):
        activity_id = kwargs['pk_activity']
        event_id = kwargs['pk_event']
        #get all days for this activity
        daylist = Day.objects.all().filter(activity=activity_id)
        for day in daylist:
            vote_value = int(request.POST[str(day.id)])
            if (vote_value == 1) or (vote_value == 0):
                voteArray = Vote.objects.all().filter(user=self.request.user,day=day)
                if not voteArray:
                    vote = Vote(day=day,will_go=bool(vote_value),user=self.request.user)
                else:
                    vote=voteArray[0]
                    vote.will_go = bool(vote_value)
                vote.save()
        return redirect('events:detail',pk_event=event_id) # Redirect after POST

