from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
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
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        image = request.FILES.get('image')  

        # Validations
        if not username and not email and not image:
            messages.warning(request, "Please update at least one field.")
            return render(request, 'blog/profile.html')
        
        if username == request.user.username and email == request.user.email and not image:
            messages.info(request, "No changes detected.")
            return render(request, 'blog/profile.html')

        if username and (len(username) <= 1 or len(username) > 30):
            messages.error(request, "Username must be between 4 and 30 characters.")
            return render(request, 'blog/profile.html')

        # Check username or email taken by another user
        if (username or email) and (User.objects.filter(username=username).exclude(pk=request.user.pk).exists() or User.objects.filter(email=email).exclude(pk=request.user.pk).exists()):
            messages.error(request, "Username or email is already taken.")
            return render(request, 'blog/profile.html')

        # Update user

        if username:
            request.user.username = username
        if email:
            request.user.email = email
        if image:
            request.user.profile.image = image
            request.user.profile.save()

        request.user.save()

        messages.success(request, "Profile updated successfully!")
        return redirect('blog_profile')

    return render(request,"blog/profile.html")