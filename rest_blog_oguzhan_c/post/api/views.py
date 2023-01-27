from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, \
    CreateAPIView, RetrieveUpdateAPIView
from rest_framework.mixins import DestroyModelMixin
from rest_framework.permissions import (
    IsAuthenticated
)

from post.api.paginations import PostPagination
# custom permissions
from post.api.permissions import IsOwner
from post.api.serializers import PostSerializer, PostUpdateCreateSerializer
from post.models import Post


# class PostListAPIView(ListAPIView, CreateModelMixin):
#     # queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     filter_backends = [SearchFilter, OrderingFilter]
#     # ordering filter için url http://localhost:8000/api/post/list?search=test&ordering=-user
#     # search filter için url http://localhost:8000/api/post/list?search=test 0
#     search_fields = ['title', 'content']
#     pagination_class = PostPagination
#
#     def get_queryset(self):
#         queryset = Post.objects.filter(draft=False)
#         return queryset
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

class PostListAPIView(ListAPIView):
    # queryset = Post.objects.all()
    # throttle_scope = 'selcuk'
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    # ordering filter için url http://localhost:8000/api/post/list?search=test&ordering=-user
    # search filter için url http://localhost:8000/api/post/list?search=test 0
    search_fields = ['title', 'content']
    pagination_class = PostPagination

    def get_queryset(self):
        queryset = Post.objects.filter(draft=False)
        return queryset


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class PostUpdateAPIView(RetrieveUpdateAPIView, DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostUpdateCreateSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwner]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateCreateSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# class PostCreateAPIView(CreateAPIView, ListModelMixin):
#     queryset = Post.objects.all()
#     serializer_class = PostUpdateCreateSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
