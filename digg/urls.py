__author__ = 'wu'

from django.conf.urls import patterns, url
from digg import views
urlpatterns = patterns('',

    url(r'digg/', views.digg)
)
