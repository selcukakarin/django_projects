"""djangoAjax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.views.generic.base import TemplateView
from rooms import views
from django.conf import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name="root/index.html"), name='index'),
    path('rooms/', TemplateView.as_view(template_name="rooms/main.html"), name='room_main'),
    path('rooms/list', views.RoomList.as_view(), name='room_list'),
    path('rooms/create', views.RoomCreate.as_view(), name='room_create'),
    path('rooms/update/<int:pk>', views.RoomUpdate.as_view(), name='room_update'),
    path('rooms/delete/<int:pk>', views.RoomDelete.as_view(), name='room_delete'),
    path('rooms/<int:pk>', views.RoomDetail.as_view(), name='room_detail'), 
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()