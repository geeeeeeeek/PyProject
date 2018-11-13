from django.shortcuts import *

def index(request):
    return render(request, 'video/index.html')

def detail(request):
    return render(request, 'video/detail.html')

def login(request):
    return render(request, 'video/login.html')

def register(request):
    return render(request, 'video/register.html')