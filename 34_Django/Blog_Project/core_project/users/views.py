from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def register(request):

    if request.user.is_authenticated:
        return redirect('blog_home')

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if(len(username) < 4) or (len(username) > 30):
            messages.error(request, "Username must be between 4 and 30 characters.")
            return render(request, 'users/register.html')
        
        if(len(email) < 4) or (len(email) > 30):
            messages.error(request, "Email must be between 4 and 30 characters.")
            return render(request, 'users/register.html')


        if password != password_confirm:
            messages.error(request, "Passwords do not match.")
            return render(request, 'users/register.html')

        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            messages.error(request, "User already registered.")
            return render(request, 'users/register.html')

        if len(password) == 0:
            messages.error(request, "Invalid password.")
            return render(request, 'users/register.html')

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request, user)
        messages.success(request, "You have successfully registered.")
        return redirect('blog_home')


    return render(request,"users/register.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect('blog_home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if(len(username) < 4) or (len(username) > 30):
            messages.error(request, "Username must be between 4 and 30 characters.")
            return render(request, 'users/login.html')
        
        if len(password) == 0:
            messages.error(request, "Invalid password.")
            return render(request, 'users/login.html')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)

            return redirect('blog_home')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'users/login.html')
    return render(request,"users/login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('user_login')