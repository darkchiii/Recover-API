from .models import Post
from collection.models import Collection
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from .serializers import PostSerializer
from rest_framework import generics, permissions, authentication
from rest_framework.response import Response
import logging
from app.permissions import IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly, IsOwner

class PostView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Create post
    def perform_create(self, serializer):
        logging.debug("perform_create method called")
        serializer.save(user=self.request.user)

# See all posts
    def get_queryset(self):
        return Post.objects.filter(Q(user=self.request.user) | Q(public=True))

# See user posts if public
class UserPosts(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Post.objects.filter(Q(user=self.kwargs['user_id']) & Q(public=True))

# See post details
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def retrieve(self, request, *args, **kwargs):
        post_instance = self.get_object()
        serializer = self.get_serializer(post_instance)

        return Response(serializer.data)

    def get_object(self):
        post_instance = super().get_object()
        print(post_instance)
        if not post_instance.public and post_instance.user != self.request.user:
            raise PermissionDenied("You don't have permission to view this post.")
        return post_instance

    def update(self, request, *args, **kwargs):
        post_instance = self.get_object()

        if 'public' in request.data:
            print("if ...")
            self.handle_public_update(post_instance, request.data['public'])

        print("standard update method called...")
        return super().update(request, *args, **kwargs)

    def handle_public_update(self, post_instance, new_public_value):
        post_instance.public = new_public_value
        post_instance.save()
        print(f"value public after saved: {post_instance.public}")
        print(f"Type of post_instance.public: {type(post_instance.public)}")

        if post_instance.public.lower() == "false":
            print(f"new public value: {new_public_value}")

            collections_with_post = Collection.objects.filter(post=post_instance)

            for collection in collections_with_post:
                collection.post.remove(post_instance)
                print(f"Post removed from collection {collection}")
            print(f"Post removed from {len(collections_with_post)} collections.")

        else:
            print("Something is fucked ^^")
