from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from favorite.api.paginations import FavoritePagination
from favorite.api.permissions import IsOwner
from favorite.api.serializers import FavoriteListCreateAPISerializer, FavoriteAPISerializer
from favorite.models import Favorite


class FavoriteListCreateAPIView(ListCreateAPIView):
    # queryset = Favorite.objects.all()
    serializer_class = FavoriteListCreateAPISerializer
    pagination_class = FavoritePagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# class FavoriteAPIView(RetrieveDestroyAPIView):
#     queryset = Favorite.objects.all()
#     serializer_class = FavoriteAPISerializer
#     lookup_field = 'pk'
#     permission_classes = [IsOwner]


# class FavoriteAPIView(RetrieveUpdateAPIView):
#     queryset = Favorite.objects.all()
#     serializer_class = FavoriteAPISerializer
#     lookup_field = 'pk'
#     permission_classes = [IsOwner]


class FavoriteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteAPISerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]
