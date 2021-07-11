from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import AudioForm
from django.http import HttpResponse, request
import subprocess

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

def Audio_store(request):
    if request.method == 'POST': 
        form = AudioForm(request.POST,request.FILES or None) 
        if form.is_valid(): 
            form.save() 
            return HttpResponse()
    else: 
        form = AudioForm() 
    return render(request, 'home.html', {'form' : form})

def separate(request):
    if request.POST:
        subprocess.run(['/home/glj/codes/music_separation/audio_web/media/scripts/demo_gao_s2s.sh'])
        if (subprocess.CompletedProcess):
            return render(request,'result.html',{})
        else:
            return render( request, "home.html",{})
