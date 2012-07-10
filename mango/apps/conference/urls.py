from django.conf.urls import patterns, include, url


urlpatterns = patterns('conference.views',
    url(r'^$', 'conference_detail', name='conference_detail'),
    url(r'^create/$', 'conference_create', name='conference_create'),
)
