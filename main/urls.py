from django.conf.urls import url
from main.views import ExtractorList, ExtractorCreate, InstanceCreate, ExtractorTypeCreate, ExtractorFileCreate, \
    ExtractorEdit

urlpatterns = [
    url(r'extractor-create$', ExtractorCreate.as_view(), name='extractor_create'),
    url(r'extractor-edit/(?P<pk>\d+)$', ExtractorEdit.as_view(), name='extractor_edit'),
    url(r'instance-create$', InstanceCreate.as_view(), name='instance_create'),
    url(r'extractor-type-create$', ExtractorTypeCreate.as_view(), name='extractor_type_create'),
    url(r'extractor-file-create$', ExtractorFileCreate.as_view(), name='extractor_file_create'),
    url(r'$', ExtractorList.as_view(), name='extractor_list'),
]
