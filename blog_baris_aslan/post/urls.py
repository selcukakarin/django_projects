from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
    path('index/', postIndex, name="index"),
    path('<slug:slug>/detail/', postDetail, name="detail"),
    path('create/', postCreate, name="create"),
    path('<slug:slug>/update/', postUpdate, name="update"),
    path('<slug:slug>/delete/', postDelete, name="delete"),
]

