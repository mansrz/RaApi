from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from Web.viewsets import *
router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'position', PositionViewSet)

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'ApiRa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'api/', include(router.urls)), #apirerstframework
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$','Web.views.home', name='home'),
    url(r'^places/', 'Web.views.placeTypes', name='types'),
    url(r'^positions', 'Web.views.positions', name='positions'),
    url(r'^map','Web.views.map', name='map'),
    url(r'^login','Web.views.login', name ='login'),
    url(r'^logout','Web.views.logout', name ='logout'),
    url(r'^search','Web.views.search', name ='search'),
    url(r'^user','Web.views.verifyUser', name ='verifyuser'),
    url(r'^update','Web.views.getPoints', name ='getpoitns'),

)
