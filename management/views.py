from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Student

def home(request):
    return render(request, 'home.html')


