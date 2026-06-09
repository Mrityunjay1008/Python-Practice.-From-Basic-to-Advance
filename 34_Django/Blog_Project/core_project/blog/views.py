from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required(login_url="user_login")
def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request,"blog/home.html",context)

@login_required(login_url="user_login")
def about(request):
    return render(request,"blog/about.html")


@login_required(login_url="user_login")
def profile(request):

    return render(request,"blog/profile.html")