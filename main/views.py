from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from main.models import Extractor, Mst_Instance, Extractor_File, Mst_Extractor_Type
from django.core.urlresolvers import reverse
from .forms import ExtractorForm

class ExtractorList(ListView):
    model = Extractor
    paginate_by = 1
    
class ExtractorCreate(CreateView):
	model = Extractor
	template_name = 'form.html'
	
	form_class = ExtractorForm
	
	def get_success_url(self):
		return reverse('extractor_list')
		
	def get_context_data(self, **kwargs):
		context = super(ExtractorCreate, self).get_context_data(**kwargs)
		context['action'] = reverse('extractor_create')
		return context
        
class ExtractorEdit(UpdateView):
	model = Extractor
	template_name = 'form.html'
	form_class = ExtractorForm
	
	def get_context_data(self, **kwargs):
		context = super(ExtractorEdit, self).get_context_data(**kwargs)
		context['action'] = reverse('extractor_edit', kwargs={'pk': self.get_object().id})
		return  context
		
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

