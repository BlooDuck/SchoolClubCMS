from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from django.shortcuts import render, redirect
import datetime


# Create your views here.

def post_list(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/post_list.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    new_comment = None
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            #new_comment.pub_date = datetime.now()
            new_comment.save()
            
            return HttpResponseRedirect('')
    else:
        form = CommentForm()
    latest_comment_list = post.comments.all()
    #latest_comment_list = Comment.objects.order_by('-pub_date')[:5]
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': latest_comment_list, 'form': form, 'new_comment':new_comment})

