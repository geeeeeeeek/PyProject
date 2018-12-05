from django.shortcuts import *
from django.views import generic
from django.contrib.auth import  authenticate,login ,logout
from django.contrib.auth.models import User
from .models import Video
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .helpers import *


@login_required(login_url='/users/login')
def add_video(request):
    Video.objects.create(title='java', desc='我是java哈哈哈')
    return HttpResponse("success")


class IndexView(generic.ListView):
    model = Video
    template_name = 'video/index.html'
    context_object_name = 'video_list'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        page_data = get_page_data(paginator, page)
        context.update(page_data)
        return context


class SearchListView(generic.ListView):
    model = Video
    template_name = 'video/search_result.html'
    context_object_name = 'video_list'
    paginate_by = 4
    q = ''

    def get_queryset(self):
        self.q = self.request.GET.get("q","")
        return Video.objects.filter(Q(title__contains=self.q))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchListView, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        page_data = get_page_data(paginator, page)
        q_data = {'q': self.q}
        context.update(page_data)
        context.update(q_data)
        return context


def detail(request):
    return render(request, 'video/detail.html')


def search_result(request):
    return render(request, 'video/search_result.html')

