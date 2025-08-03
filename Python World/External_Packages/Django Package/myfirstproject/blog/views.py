from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post

# Create your views here.

def home(request):
    return HttpResponse("You're at the home page.")

def about(request):
    return HttpResponse("You're at the about page.")

def hello_user(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")

def post_detail(request, id_number):
    post = get_object_or_404(Post, id=id_number)
    # return HttpResponse(f"<h1>{post.title}</h1><p>{post.body}</p>")
    return render(request, 'blog/post_detail.html', {'post': post})

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

