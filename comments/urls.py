from django.urls import path
from .views import CommentListCreateView, CommentDetailView, CommentLikeView

urlpatterns = [
    path('post/<int:post_id>/comments/', CommentListCreateView.as_view(), name='create-list-comment'),
    path('comment/<int:comment_id>/', CommentDetailView.as_view(), name='comment-details'),
    path('like/comment/<int:comment_id>/', CommentLikeView.as_view(), name='comment-like'),
]
