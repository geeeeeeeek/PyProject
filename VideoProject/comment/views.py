from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,JsonResponse
from video.forms import CommentForm
from video.models import Video

from django.template.loader import render_to_string

from datetime import datetime
from ratelimit.decorators import ratelimit

# Create your views here.

@ratelimit(key='ip', rate='2/m')
def submit_comment(request,pk):
    was_limited = getattr(request, 'limited', False)
    if was_limited:
        return JsonResponse({"code": 1, 'msg': '评论太频繁了'})
        pass
    video = get_object_or_404(Video, pk = pk)
    form = CommentForm(data=request.POST)

    if form.is_valid():
        # print('success')
        new_comment = form.save(commit=False)
        new_comment.user = request.user
        new_comment.nickname = request.user.nickname
        new_comment.video = video
        new_comment.save()

        data = dict()
        data['nickname'] = request.user.nickname
        data['timestamp'] = datetime.fromtimestamp(datetime.now().timestamp())
        data['content'] = new_comment.content

        comments = list()
        comments.append(data)

        html = render_to_string(
            "comment/comment_single.html", {"comments": comments})

        return JsonResponse({"code":0,"html": html})
    return JsonResponse({"code":1,'msg':'评论失败!'})