from django.shortcuts import *

def index(request):
    return render(request, 'video/index.html')

def detail(request):
    return render(request, 'video/detail.html')

def login(request):
    return render(request, 'video/login.html')

def register(request):
    return render(request, 'video/register.html')

def logout(request):
    return HttpResponse("logout success")

def profile(request):
    return render(request, 'video/profile.html')

def settings(request):
    return render(request, 'video/settings.html')

def account_setting(request):
    return render(request, 'video/account_setting.html')

def bookmarks(request):
    return render(request, 'video/bookmarks.html')

def like_videos(request):
    return render(request, 'video/like_videos.html')