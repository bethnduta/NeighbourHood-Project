
from django.urls import path
from . import views
from .views import PostListView,PostDetailView


urlpatterns = [
    path('',views.home,name='home'),
    path('index/', PostListView.as_view(), name='index'),
    path('about/', views.neighbor, name='about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.post_create, name='post-create'),
    path('neighborhood',views.neighborhood,name='neighborhood'),
    # path('new_neighborhood',views.new_neighborhood,name='new_neighborhood'),
    # path('single_neighborhood/<int:pk>/',views.single_neighborhood,name='single_neighborhood'),
    # path('new_neighborhood/<int:pk>/',views.new_neighborhood,name='new_neighborhood'),
    # path('leave_neighborhood/<int:pk>/',views.leave_neighborhood,name='leave_neighborhood'),
    # path('business/',views.business,name='business'),
    # path('new_business/',views.new_business,name='new_business'),
    # path('search/',views.search_business,name='search'),
]