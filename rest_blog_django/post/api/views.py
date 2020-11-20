from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (
                                        ListAPIView,
                                        RetrieveAPIView,
                                        DestroyAPIView,
                                        UpdateAPIView,
                                        CreateAPIView,
                                        RetrieveUpdateAPIView,

                                    )
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin

from post.api.paginations import PostPagination
from post.api.permissions import IsOwner
from post.api.serializers import PostSerializer, PostUpdateCreateSerializer
from post.models import Post
from rest_framework.permissions import (
                                            IsAuthenticated,
                                            IsAdminUser
                                        )


class PostListAPIView(ListAPIView, CreateModelMixin):
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    pagination_class = PostPagination

    def get_queryset(self):
        queryset = Post.objects.filter(draft=False)
        return queryset

    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


# class PostDeleteAPIView(DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = 'slug'
#     permission_classes = [IsOwner]


class PostUpdateAPIView(RetrieveUpdateAPIView, DestroyModelMixin):
    queryset = Post.objects.all()
    # serializer_class = PostUpdateCreateSerializer
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwner]

    def destroy(self, request, *args, **kwargs):
        return self.destroy(DestroyModelMixin)

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)
        # article'a burada en son değiştiren kullanıcı eklenebilir


class PostCreateAPIView(CreateAPIView, ListModelMixin):
    queryset = Post.objects.all()
    # serializer_class = PostUpdateCreateSerializer
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        # mail gönderme yapılabilir
