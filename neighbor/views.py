from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def neighbor(request):
    return HttpResponse(request,"Hello, world. You're at the neighbor index.")    