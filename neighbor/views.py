from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import post
from .forms import UserRegisterForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView,  UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import PostForm

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
        return redirect('login')
        
    else:    
        form = UserRegisterForm()
    return render(request,'register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Account updated successfully')
            return redirect('profile')
    u_form=UserUpdateForm(instance=request.user)
    p_form=ProfileUpdateForm(instance=request.user)

    context={'u_form':u_form,'p_form':p_form}
    return render(request,'profile.html',context)


class PostListView(ListView):
    model = post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = post
    template_name = 'detail.html'

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form) 


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=post 
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False