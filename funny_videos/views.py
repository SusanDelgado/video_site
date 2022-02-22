from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Video
from django.urls import reverse_lazy
from .forms import PostForm
from django.views.generic import ListView, CreateView

def index(request):
    videos = Video.objects.all()
    template = loader.get_template('funny_videos/video.html')
    context = {'videos': videos}

    return HttpResponse(template.render(context, request))

class add_new(CreateView):
    model = Video  
    form_class = PostForm
    template_name = 'funny_videos/add_new.html'
    success_url = reverse_lazy('index')



