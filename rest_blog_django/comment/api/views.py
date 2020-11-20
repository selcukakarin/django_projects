from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin

from comment.api.serializers import CommentCreateSerializer, CommentListSerializer, CommentDeleteUpdateAPISerializer
from comment.models import Comment
from comment.api.paginations import CommentPagination
from comment.api.permissions import IsOwner

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer
    pagination_class = CommentPagination
    def get_queryset(self):
        queryset = Comment.objects.filter(parent = None)
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(post = query)
        return queryset


# class CommentDeleteAPIView(DestroyAPIView, UpdateModelMixin, RetrieveModelMixin):
#     queryset = Comment.objects.all()
#     serializer_class = CommentDeleteUpdateAPISerializer
#     lookup_field = 'pk'
#     permission_classes = [IsOwner]

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(self, request, *args, **kwargs)


class CommentUpdateAPIView(DestroyModelMixin, RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteUpdateAPISerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

