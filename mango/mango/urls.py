import os

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'generic.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    # Django Social Auth
    url(r'', include('social_auth.urls')),
    # Django Mango
    url(r'proposal/', include('proposal.urls')),
    url(r'speakers/', include('speakers.urls')),
    url(r'conference/', include('conference.urls')),
)

if settings.DEBUG:
    generic_static_path = os.path.join(
        settings.PROJECT_ROOT, 'mango', 'generic', 'static')
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$',
         'django.views.static.serve',
         {'document_root': generic_static_path}),
        (r'^favicon\.ico$',
         'django.views.generic.simple.redirect_to',
         {'url': '/static/favicon.ico'}),
    )
