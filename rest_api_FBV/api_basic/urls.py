
from django.urls import path, include
from api_basic.views import article_list, article_detail

app_name = 'article'

urlpatterns = [
    path('article/', article_list),
    path('detail/<int:pk>', article_detail),

]