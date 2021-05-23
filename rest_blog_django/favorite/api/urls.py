from django.urls import path, include

from favorite.api.views import FavoriteListCreateAPIView, FavoriteAPIView

app_name = 'favorite'

urlpatterns = [
    path('list_create', FavoriteListCreateAPIView.as_view(), name='list_create'),
    path('update_delete/<pk>', FavoriteAPIView.as_view(), name='update_delete'),
]
