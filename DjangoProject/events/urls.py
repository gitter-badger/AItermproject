from django.conf.urls import patterns, url

from events import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk_event>\d+)/$', views.EventDetail.as_view(), name='detail'),
    url(r'^(?P<pk_event>\d+)/result/$', views.EventCSPResultDetail.as_view(), name='result'),
    url(r'^(?P<pk_event>\d+)/activity/(?P<pk_activity>\d+)/$', views.ActivityDetailView.as_view(), name='activitydetail'),
)
