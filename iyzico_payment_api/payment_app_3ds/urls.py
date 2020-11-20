from django.urls import path, include
from . import views

app_name = 'payment_app_3ds'

urlpatterns = [
    path('pay_init', views.pay_init, name="pay_init")
]
