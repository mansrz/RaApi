from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'ApiRa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','Web.views.home', name='home'),
    url(r'^places/', 'Web.views.placeTypes', name='types'),
    url(r'^positions', 'Web.views.positions', name='positions'),
    url(r'^map','Web.views.map', name='map'),
    url(r'^login','Web.views.login', name ='login'),
    url(r'^logout','Web.views.logout', name ='logout'),
    url(r'^search','Web.views.search', name ='search'),

)
