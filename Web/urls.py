from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ApiRa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^places/', 'Web.views.PlaceTypes', name='types'),
)
