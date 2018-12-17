from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import *
from django.views import generic
from VideoProject.helpers import get_page_data, ajax_required, ajax_login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_http_methods

from django.template.loader import render_to_string
from django.http import HttpResponseBadRequest, JsonResponse
from .models import Video
from comment.models import Comment
from .forms import CommentForm


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


class VideoDetailView(generic.DetailView):
    model = Video
    template_name = 'video/detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.view_count += 1
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super(VideoDetailView, self).get_context_data(**kwargs)
        # 推荐数据
        recommend_list = Video.objects.order_by('-view_count')[:4]
        recommend_data = {'recommend_list':recommend_list}

        form = CommentForm()
        form_data = {'form':form}
        context.update(recommend_data)
        context.update(form_data)
        return context

@login_required
@ajax_required
@require_http_methods(["POST"])
def like(request):
    video_id = request.POST['video_id']
    video = Video.objects.get(pk=video_id)
    user = request.user
    video.switch_like(user)
    return JsonResponse({"code": 0, "likes": video.count_likers(), "user_liked": video.user_liked(user)})


@login_required
@ajax_required
@require_http_methods(["POST"])
def collect(request):
    video_id = request.POST['video_id']
    video = Video.objects.get(pk=video_id)
    user = request.user
    video.switch_collect(user)
    return JsonResponse({"code": 0, "collects": video.count_collecters(), "user_collected": video.user_collected(user)})


# todo 今晚整理代码
def get_comments(request):
    if not request.is_ajax():
        return HttpResponseBadRequest()
    page = request.GET.get('page')
    video_id = request.GET.get('video_id')
    video = get_object_or_404(Video, pk=video_id)
    comments = video.comment_set.order_by('-timestamp').all()
    comment_count = len(comments)
    print(comment_count)

    paginator = Paginator(comments, 15)
    try:
        rows = paginator.page(page)
    except PageNotAnInteger:
        rows = paginator.page(1)
    except EmptyPage:
        rows = []

    if len(rows) > 0:
        code = 0
        html = render_to_string(
            "comment/comment_single.html", {"comments": rows})
    else:
        code = 1
        html = ""

    return JsonResponse({
        "code":code,
        "html": html,
        "comment_count": comment_count
    })

