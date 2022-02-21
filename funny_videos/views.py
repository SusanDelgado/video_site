from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Video

def index(request):
    videos = Video.objects.all()
    template = loader.get_template('funny_videos/video.html')
    context = {'videos': videos}

    return HttpResponse(template.render(context, request))

# Create your views here.
