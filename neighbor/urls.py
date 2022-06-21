
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, post_create, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('about/', views.neighbor, name='about'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', post_create, name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('search/',views.search,name='search1'),
    path('api/post/',views.PostView.as_view(),name='apipost'),
]