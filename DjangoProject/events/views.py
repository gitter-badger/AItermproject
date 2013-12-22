from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic

from events.models import *
from events.forms import *
import pdb

class IndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'all_event_list'

    def get_queryset(self):
        """
        Return all events
        """
        return Event.objects.all().order_by('-pub_date')

class DetailView(generic.DetailView):
    pk_url_kwarg = 'pk_event' #I find more clear to use this name than only pk
    model = Event
    template_name = 'events/detail.html'


class ActivityDetailView(generic.DetailView):
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
            fields.append({'name': str(day.id), 'label': day.day })

        context['voteform'] = MultiVoteForm(dynamic_fields=fields)

        return context

'''class ActivityIndexView(generic.ListView):
    template_name = 'activities/index.html'
    context_object_name = 'all_activities_list'

    def get_queryset(self):
        """
        Return the activities for the specified event
        """
        return Activity.objects.all().filter(event=self.kwargs['pk_event'])'''


class EventCreate(generic.CreateView):
    model = Event
    template_name = 'events/create.html'
    form_class = EventForm


def vote(request, pk_event, pk_activity):
    if request.method == 'POST': # If the form has been submitted...
        #get all days for this activity
        daylist = Day.objects.all().filter(activity=pk_activity)
        for day in daylist:
            vote_value = int(request.POST[str(day.id)])
            #pdb.set_trace()
            if (vote_value == 1) or (vote_value == 0):
                vote = Vote(day=day,will_go=bool(vote_value))
                vote.save()
        return redirect('events:detail',pk_event=pk_event) # Redirect after POST

    return redirect('events:activitydetail', pk_event=pk_event, pk_activity=pk_activity)

