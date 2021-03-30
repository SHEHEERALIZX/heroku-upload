from django.shortcuts import render
from .models import Post

# Create your views here.
from django.views.generic import ListView, DetailView

class BlogView(ListView):
    model = Post

    template_name = 'home.html'
    context_object_name = 'posts'
    slug_field = 'title'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogview.html'
    context_object_name = 'messages'    