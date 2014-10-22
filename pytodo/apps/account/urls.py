from django.conf.urls import patterns, url

urlpatterns = patterns('',
            url(r'^$', 'pytodo.apps.account.views.index' ),
            url(r'^new/$', 'pytodo.apps.account.views.new'),
            url(r'^profile/$', 'pytodo.apps.account.views.profile')
        )
