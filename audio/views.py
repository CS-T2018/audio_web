from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
