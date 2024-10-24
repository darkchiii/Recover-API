from django.urls import path
from .views import CollectionView, CollectionDetailView, SavePostView, UserCollectionView

urlpatterns = [
    path('', CollectionView.as_view(), name='create-list-collection'),
    path('<int:id>/', CollectionDetailView.as_view(), name='collection-detail-view'),
    path('post/<int:post_id>/', SavePostView.as_view(), name='save-post-to-collection'),
    path('<int:collection_id>/post/<int:post_id>/', SavePostView.as_view(), name='save-post-to-collection'),
    path('user/<int:user_id>/', UserCollectionView.as_view(), name='user-collections'),
]