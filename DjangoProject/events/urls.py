from django.conf.urls import patterns, url

from events import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk_event>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk_event>\d+)/activity/(?P<pk_activity>\d+)/$', views.ActivityDetailView.as_view(), name='activitydetail'),
    url(r'^(?P<pk_event>\d+)/activity/(?P<pk_activity>\d+)/vote/$', views.vote, name='vote'),
)
#url(r'^(?P<pk_event>\d+)/activity/$', views.ActivityIndexView.as_view(), name='activityindex'),
#url(r'^(?P<pk_event>\d+)/results/$', views.ResultsView.as_view(), name='results'),
