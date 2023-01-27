from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, \
    RetrieveUpdateDestroyAPIView

from favorite.api.paginations import FavoritePagination
from favorite.api.permissions import IsOwner
from favorite.api.serializers import FavoriteListCreateAPISerializer, FavoriteAPISerializer
from favorite.models import Favorite
from rest_framework.permissions import IsAuthenticated


class FavoriteListCreateAPIView(ListCreateAPIView):
    serializer_class = FavoriteListCreateAPISerializer
    pagination_class = FavoritePagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavoriteRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = FavoriteAPISerializer
    queryset = Favorite.objects.all()
    lookup_field = 'pk'
    permission_classes = [IsOwner]


class FavoriteRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = FavoriteAPISerializer
    queryset = Favorite.objects.all()
    lookup_field = 'pk'
    permission_classes = [IsOwner]

class FavoriteRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = FavoriteAPISerializer
    queryset = Favorite.objects.all()
    lookup_field = 'pk'
    permission_classes = [IsOwner]
