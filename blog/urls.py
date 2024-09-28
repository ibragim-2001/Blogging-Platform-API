from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostsView.as_view(), name='posts'),
    path('posts/<int:id>/', views.PostView.as_view(), name='post_detail'),
]