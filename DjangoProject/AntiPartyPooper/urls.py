from django.conf.urls import patterns, include, url
from AntiPartyPooper import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AntiPartyPooper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^events/', include('events.urls',namespace="events")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^accounts/', include('registration.backends.simple.urls'),name='accounts'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': 'index'}),
)
#url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'}),
#url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'index'}),
