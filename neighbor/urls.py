
from django.urls import path
from . import views
from .views import PostListView,PostDetailView


urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('about/', views.neighbor, name='about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.post_create, name='post-create'),
    path('search/',views.search,name='search1'),
]