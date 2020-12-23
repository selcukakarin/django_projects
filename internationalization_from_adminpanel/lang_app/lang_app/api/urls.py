from .views import *
from django.conf.urls import url, include
from django.urls import path

urlpatters = [path('translate/', translate_view),]