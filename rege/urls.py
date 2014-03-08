__author__ = 'wu'
from django.conf.urls import patterns, url
from rege import views
urlpatterns = patterns('',

    url(r'login/', views.log_in),
    url(r'logout/', views.log_out),
    url(r'register/', views.register),
)

