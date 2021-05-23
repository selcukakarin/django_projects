from django.contrib import admin
from django.urls import path
from post.api.views import (
    PostListAPIView,
    PostDetailAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView,
    PostCreateAPIView
)

app_name = 'post'

urlpatterns = [
    path('list/', PostListAPIView.as_view(), name='list'),
    path('detail/<slug>', PostDetailAPIView.as_view(), name='detail'),
    path('delete/<slug>', PostDeleteAPIView.as_view(), name='delete'),
    path('update/<slug>', PostUpdateAPIView.as_view(), name='update'),
    path('create/', PostCreateAPIView.as_view(), name='create')
]
