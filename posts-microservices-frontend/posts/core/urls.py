
from django.urls import path, include
from .views import PostAPIView, PostCommentAPIView

urlpatterns = [
    path('posts', PostAPIView.as_view()),
    path('posts/<str:pk>/comments', PostCommentAPIView.as_view())
]
