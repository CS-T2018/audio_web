from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import AudioForm
from django.urls import reverse
from django.http import HttpResponse, request
from .OpenUnmix import demo_gao_s2s


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

def Audio_store(request):
    if request.method == 'POST': 
        form = AudioForm(request.POST,request.FILES or None) 
        if form.is_valid(): 
            form.save() 
            return HttpResponse()
    else: 
        form = AudioForm() 
    return render(request, 'home.html', {'form' : form})

def Separate(request):
    if request.method == 'POST' and 'run_script' in request.POST:  
        # call function
        demo_gao_s2s()
        # return user to required page
        return HttpResponseRedirect(reverse('audio',HomePageView))