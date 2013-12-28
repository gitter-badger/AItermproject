from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.detail import SingleObjectMixin
from events.models import *
from events.forms import *
import pdb

class IndexView(ListView):
    template_name = 'events/index.html'
    context_object_name = 'all_event_list'
    model = Event

class EventDetail(DetailView):
    pk_url_kwarg = 'pk_event' #I find more clear to use this name than only pk
    model = Event
    template_name = 'events/detail.html'


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
            fields.append({'name': str(day.id), 'label': day.day })
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
                vote = Vote(day=day,will_go=bool(vote_value),user=self.request.user)
                vote.save()
        return redirect('events:detail',pk_event=event_id) # Redirect after POST


class EventCreate(CreateView):
    model = Event
    template_name = 'events/create.html'
    form_class = EventForm

    def post(self, request, *args, **kwargs):
        eform = EventForm(request.POST, instance=Event())
        aforms = [ActivityForm(request.POST, prefix=str(x), instance=Activity()) for x in range(0,3)]
        if eform.is_valid() and all([af.is_valid() for af in aforms]):
            new_event = eform.save()
            for af in aforms:
                new_activity = af.save(commit=False)
                new_activity.event = new_event
                new_activity.save()
            return HttpResponseRedirect('/events/add/')
        return render_to_response(self.template_name, {'event_form': eform, 'activity_forms': aforms})
    def get(self, request, *args, **kwargs):
        eform = EventForm(instance=Event())
        aforms = [ActivityForm(prefix=str(x), instance=Activity()) for x in range(0,3)]
        return render_to_response(self.template_name, {'event_form': eform, 'activity_forms': aforms})


