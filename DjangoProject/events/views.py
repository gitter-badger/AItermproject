from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from events.models import *

class IndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'all_event_list'

    def get_queryset(self):
        """
        Return all events
        """
        return Event.objects.all().order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'


class ResultsView(generic.DetailView):
    model = Event
    template_name = 'events/results.html'


def vote(request, event_id):
    p = get_object_or_404(Event, pk=event_id)
    try:
        selected_Activity = p.Activity_set.get(pk=request.POST['Activity'])
    except (KeyError, Activity.DoesNotExist):
        # Redisplay the event voting form.
        return render(request, 'events/detail.html', {
            'event': p,
            'error_message': "You didn't select a Activity.",
        })
    else:
        selected_Activity.votes += 1
        selected_Activity.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('events:results', args=(p.id,)))