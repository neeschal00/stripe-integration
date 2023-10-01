from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.contrib.auth import views as auth_views #to avoid yk
from users import views as user_views

def index(request):
    return HttpResponse("This is a response")

urlpatterns = [
    path('register/',user_views.registerview,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html',redirect_authenticated_user=True),name='login'),
]
