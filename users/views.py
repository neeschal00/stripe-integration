from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.views.generic import TemplateView
# Create your views here.

def registerview(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created! You are able to login')
            return redirect('login')
    else:
        # form = UserCreationForm()
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form': form})







