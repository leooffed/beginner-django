from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Post

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'