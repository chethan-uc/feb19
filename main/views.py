from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView,CreateView
from main.models import Extractor

class ExtractorList(ListView):
    model = Extractor
