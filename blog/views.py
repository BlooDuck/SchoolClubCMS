from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from .models import Post, Comment
from django.shortcuts import render


# Create your views here.

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/index.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    latest_comment_list = Comment.objects.order_by('-pub_date')[:5]
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': latest_comment_list})
