from django.conf.urls import patterns, include, url

from django.contrib import admin
from home.views import index, search
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'home.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^home/$', index),
    url(r'search/', search),
    url(r'^admin/', include(admin.site.urls)),
    url(r'digg/', include('digg.urls')),
    url(r'rege/', include('rege.urls')),
)
