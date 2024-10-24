from django.forms import ValidationError
from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Collection
from posts.models import Post
from .serializers import CollectionSerializer
from django.core.exceptions import ObjectDoesNotExist
from app.permissions import IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly
import logging

logger = logging.getLogger(__name__)

class CollectionView(generics.ListCreateAPIView):
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# See collections made by user making request
    def get_queryset(self):
        user = self.request.user
        # logger.debug(f"User {user} collections")
        return Collection.objects.filter(user=user)

# Create collection
    def perform_create(self, serializer):
        user=self.request.user
        title = self.request.data.get('title')

        if Collection.objects.filter(user=user, title=title).exists():
            raise ValidationError("You already have collection with this title.")
        serializer.save(user=user, title=title)

# See user public collections
class UserCollectionView(generics.ListAPIView):
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Collection.objects.filter(Q(user=self.kwargs['user_id']) & Q(public=True)) # & Q(post__public=True)

# See collection details
class CollectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'id'

    def get_queryset(self):
        collection_id = self.kwargs['id']
        logger.debug(f"Fetching collection with ID: {collection_id}")
        try:
            collection = Collection.objects.filter(Q (id=collection_id, user=self.request.user) | Q(id=collection_id, public=True))
        except Collection.DoesNotExist:
            logger.debug(f"Collection not found..")
            return Response({"detail": "Collection not found."}, status=status.HTTP_404_NOT_FOUND)
        logger.debug(f"Collection found..")
        return collection


# Save post to collection
class SavePostView(generics.CreateAPIView):
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        post_id = self.kwargs['post_id']
        collection_id = self.kwargs.get('collection_id', None)
        title = request.data.get('title', None)
        # logger.debug(f"User: {user}")
        # logger.debug(f"Post ID: {post_id}")
        # logger.debug(f"Collection ID: {collection_id}")
        # logger.debug(f"Title: {title}")

        if not title:
            collection_count = Collection.objects.filter(user=user).count()
            title = f"Collection {collection_count+1}"
            # logger.debug(f"Generated title: {title}")
        try:
            post = Post.objects.get(id=post_id, public=True)
            # logger.debug(f"Post found: {post}")
        except Post.DoesNotExist:
            logger.error("Post not found")
            return Response({"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

        if collection_id:
            try:
                collection = Collection.objects.get(id=collection_id, user=user)
                # logger.debug(f"Collection found: {collection}") # w logu brak id
            except Collection.DoesNotExist:
                # logger.error("Collection not found")
                return Response({"detail:" "Collection not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            collection = Collection.objects.create(user=user, title=title)
            logger.debug(f"Collection created: {collection}")

        collection.post.add(post)
        collection.save()

        post.saves += 1
        post.save()
        # logger.debug(f"Post added to collection: {collection}") # w logu brak id

        collection_serializer = CollectionSerializer(collection)
        # logger.debug(f"Serialized collection: {collection_serializer.data}")
        return Response(collection_serializer.data, status=status.HTTP_200_OK)
