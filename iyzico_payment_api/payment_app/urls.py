from django.urls import path, include
from . import views

app_name = 'payment_app'

urlpatterns = [
    path('pay', views.pay, name="pay")
]
