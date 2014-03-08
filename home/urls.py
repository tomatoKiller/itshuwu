from django.conf.urls import patterns, include, url

from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'home.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'reqhandle/', include('reqhandle.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'digg/', include('digg.urls')),
    url(r'rege/', include('rege.urls')),
)
