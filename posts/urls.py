from django.urls import path
from .views import PostView, PostDetailView, UserPosts

urlpatterns = [
    path('post/', PostView.as_view(), name='post-list-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:user_id>/', UserPosts.as_view(), name='user-posts'),
]