from django.shortcuts import render
from .models import Post


def blog_list(request):
    post =Post.objects.all()
    context={
        
        'blog_list':post

         }
    return render(request,"innovate_nepal/blog_list.html",context)


def blog_detail(request,id):
    each_post=Post.objects.get(id= id)
    context={
        
        'blog_detail':each_post
        
        }
    return render(request,'innovate_nepal/blog_detail.html',context)
