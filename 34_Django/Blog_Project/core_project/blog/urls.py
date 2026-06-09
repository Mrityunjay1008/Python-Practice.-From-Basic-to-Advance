from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="blog_home"),
    path("about/", views.about, name="blog_about"),
    path("profile/", views.profile, name="blog_profile"),
] 
