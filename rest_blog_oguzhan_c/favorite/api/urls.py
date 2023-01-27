from django.urls import path

from favorite.api.views import FavoriteListCreateAPIView, FavoriteRetrieveUpdateAPIView, FavoriteRetrieveDestroyAPIView, \
    FavoriteRUDAPIView

app_name = "favorite"
urlpatterns = [
    path('list-create', FavoriteListCreateAPIView.as_view(), name='list-create'),
    path('update-retrieve/<pk>', FavoriteRetrieveUpdateAPIView.as_view(), name='update-retrieve'),
    path('delete-retrieve/<pk>', FavoriteRetrieveDestroyAPIView.as_view(), name='delete-retrieve'),
    path('rud/<pk>', FavoriteRUDAPIView.as_view(), name='rud'),
]
