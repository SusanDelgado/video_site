from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('At this page will be some funny videos')

# Create your views here.
