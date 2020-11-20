
from django.urls import path, include
from .views import home, article_entry, article_list

app_name="article"

urlpatterns = [
    path('', home, name='home'),
    path('article_entry/', article_entry, name='article_entry'),
    path('article_list/', article_list, name='article_list'),
]
