from . import views
from django.urls import path

urlpatterns = [
    path("register/", views.register, name="user_register"),
    path("login/", views.login_view, name="user_login"),
    path("logout/", views.logout_view, name="user_logout"),
]
