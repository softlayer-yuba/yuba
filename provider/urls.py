from django.conf.urls import patterns, include, url

urlpatterns = patterns('provider.views',
    url(r'^$', 'index'),
)
