from django.urls import path, include

from account.api.views import (
                                ProfileView,
                                UpdatePassword,
                                CreateUserView
                            )

app_name = 'account'

urlpatterns = [
    path('me/<pk>', ProfileView.as_view(), name='me'),
    path('change_password', UpdatePassword.as_view(), name='change_password'),
    path('register', CreateUserView.as_view(), name='register'),

]
