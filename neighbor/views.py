from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import post
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    context = {'posts':post.objects.all()}
    return render(request, 'index.html', context)

def neighbor(request):
    return render(request, 'about.html',{'title':'neighbor'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            
        return redirect('/')
        
    else:    
        form = UserRegisterForm()
    return render(request,'register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'profile.html')