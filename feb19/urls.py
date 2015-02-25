from django.conf.urls import patterns, include, url

from django.contrib import admin
from main import urls as main_urls #s2
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^main/', include(main_urls)), #s2
)
