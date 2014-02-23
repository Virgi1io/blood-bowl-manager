from django.conf.urls import patterns, url

urlpatterns = patterns('manager.views',
    url(r'^$', 'home'),
    url(r'^coaches/$', 'coach_list'),
)
