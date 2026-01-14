from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def library(request):
    return render(request, 'main/library.html')

def dictionary(request):
    return render(request, 'main/dictionary.html')

def prevention(request):
    return render(request, 'main/prevention.html')

def contact(request):
    return render(request, 'main/contact.html')
