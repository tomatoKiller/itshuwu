__author__ = 'wu'
from django.conf.urls import patterns, url

from reqhandle.views import comment, search, index, getcomment, recommend

urlpatterns = patterns('',
    url(r'index/', index),
    url(r'getcomment/', getcomment),
    url(r'comment/$', comment),
    url(r'search/', search),
    url(r'recommend/', recommend),
)
