from django.conf.urls import patterns, url
from main.views import ExtractorList

urlpatterns = patterns('main.views',
	url(r'list', ExtractorList.as_view(), name='extractor_list')
)
