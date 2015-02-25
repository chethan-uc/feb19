from django.conf.urls import patterns, url
from main.views import ExtractorList, ExtractorCreate, InstanceCreate, ExtractorTypeCreate, ExtractorFileCreate

urlpatterns = patterns('main.views',
	url(r'$', ExtractorList.as_view(), name='extractor_list'),
	url(r'extractor-create$', ExtractorCreate.as_view(), name='extractor_create'),
	url(r'instance-create$', InstanceCreate.as_view(), name='instance_create'),
	url(r'extractor-type-create$', ExtractorTypeCreate.as_view(), name='extractor_type_create'),
	url(r'extractor-file-create$', ExtractorFileCreate.as_view(), name='extractor_file_create'),
)
