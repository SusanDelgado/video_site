from django.urls import path
from . import views
from .views import add_new

urlpatterns = [
    path('add_new/', add_new.as_view(), name = 'add_new'),
    path('',views.index, name = 'index'),
]
