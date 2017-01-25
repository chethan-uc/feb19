from django.conf.urls import include, url
from django.contrib import admin
from main import urls as main_urls  # s2

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(main_urls)),  # s2
]
