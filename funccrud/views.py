from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import NewBlog

def welcome(request):
    return render(request, 'funccrud/index.html')

def read(request):
    return

def create(request):
    return

def update(request, pk):
    return

def delete(request, pk):
    return
# Create your views here.
