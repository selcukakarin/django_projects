
from django.urls import path
from .views import pay, payment_result

app_name = 'app1'

urlpatterns = [
    path('pay', pay, name="pay"),
    path('payment_result', payment_result, name="payment_result"),
]
