from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pytodo.views.home', name='home'),
    url(r'^', include('pytodo.apps.account.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
