from django.shortcuts import render, get_object_or_404

from .models import Blog

def allblogs(req):
    blogs = Blog.objects
    return render(req, 'blog/allblogs.html', {'blogs':blogs})

def detail(req, blog_id):
    fullblog = get_object_or_404(Blog, pk=blog_id)
    return render(req, 'blog/detail.html', {'blog':fullblog})
