from django.contrib.auth import authenticate, login, logout
from django.shortcuts import *
from django.views import generic
from django.contrib.auth import get_user_model
User = get_user_model()

class LoginView(generic.View):

    def get(self,request):
        next = request.GET.get('next', '')
        return render(request, "users/login.html", {'next': next})

    def post(self,request):
        user = authenticate(username=request.POST.get('username', ''),
                            password=request.POST.get('password', ''))
        if user is not None:
            login(request, user)
            next = request.POST.get('next')
            if next in [None,'']:
                next = '/video/index'
            return HttpResponseRedirect(next)
        else:
            return render(request, 'users/login.html',{'msg':'用户名或密码错误'})

class RegisterView(generic.View):

    def get(self,request):
        return render(request, 'users/register.html')

    def post(self,request):
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username == '' or password == '':
            return render(request, 'users/register.html',{'msg':'注册失败'})
        else:
            user = User.objects.create_user(username, password=password)
            user.save()
            return HttpResponseRedirect(reverse('users:login'))

class LogoutView(generic.View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse('video:index'))

def profile(request):
    return render(request, 'users/profile.html')

def settings(request):
    return render(request, 'users/settings.html')

def account_setting(request):
    return render(request, 'users/account_setting.html')

def bookmarks(request):
    return render(request, 'users/bookmarks.html')

def like_videos(request):
    return render(request, 'users/like_videos.html')