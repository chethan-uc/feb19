from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from main.models import Extractor, Mst_Instance, Extractor_File, Mst_Extractor_Type
from django.core.urlresolvers import reverse

class ExtractorList(ListView):
    model = Extractor
    
    
class ExtractorCreate(CreateView):
    model = Extractor
    template_name = 'form.html'
    
    def get_success_url(self):
        return reverse('extractor_list')
class InstanceCreate(CreateView):
    model = Mst_Instance
    template_name = 'form.html'
    
    def get_success_url(self):
        return reverse('extractor_list')
    
class ExtractorFileCreate(CreateView):
    model = Extractor_File
    template_name = 'form.html'
    def get_success_url(self):
        return reverse('extractor_list')
    
class ExtractorTypeCreate(CreateView):
    model = Mst_Extractor_Type
    template_name = 'form.html'
    def get_success_url(self):
        return reverse('extractor_list')

