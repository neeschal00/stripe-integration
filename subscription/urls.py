from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.contrib.auth import views as auth_views #to avoid yk
from .views import *


urlpatterns = [
    path("stripe-webhook/",webhook_portal,name="stripe-webhook")
]
