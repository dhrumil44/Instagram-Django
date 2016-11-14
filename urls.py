from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^profile/$', views.profile),
    url(r'^search/$', views.search),
    url(r'^profile/(?P<username>\w+)/(?P<friend1>\w+)/$', views.profileRequest),
    url(r'^friends/$', views.friends),
    url(r'^register/$', views.register),
    url(r'^login/$', views.loginpage),
    url(r'^logout/$', views.logoutpage),
    url(r'^upload/$', views.upload)
]
