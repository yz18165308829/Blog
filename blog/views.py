from django.shortcuts import render, get_object_or_404
import markdown
# Create your views here.

from django.http import HttpResponse

from .models import Post, Category,Tag


def index(request):
    posts = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'posts': posts,
        'title': '我的博客首页'
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'post': post})


def archives(request, year, month):
    posts = Post.objects.filter(created_time__year=year,
                                created_time__month=month
                                ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'posts': posts})


def category(request, id):
    #获取分类信息
    category = Category.objects.get(pk=id)
    posts = Post.objects.filter(category=category).order_by('-created_time')
    return render(request, 'blog/index.html', context={'posts': posts})


def tags(request,id):
    #获取标签信息
    tags=Tag.objects.get(pk=id)
    posts=Post.objects.filter(tags=tags).order_by('-created_time')
    return render(request,'blog/index.html',context={'posts':posts})

