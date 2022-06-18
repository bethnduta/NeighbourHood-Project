from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts=[
    {
        'author':'CoreyMS',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'August 27, 2018'
    },
    {
        'author':'Jane Doe',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'August 28, 2018'
    }
]
def index(request):
    context = {'posts':posts}
    return render(request, 'index.html', context)

def neighbor(request):
    return render(request, 'about.html',{'title':'neighbor'})