"""vitor_beginners_guide URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from boards.views import (
                            # home,  # FOR FBV
                            # board_topics,  # FOR FBV
                            new_topic, 
                            # topic_posts,   # FOR FBV
                            reply_topic,  
                            PostUpdateView,
                            BoardListView,
                            TopicListView,
                            PostListView,
                            )
from accounts.views import signup, UserUpdateView
from django.contrib.auth.views import (
                                        LogoutView,
                                        LoginView, 
                                        PasswordResetView,
                                        PasswordResetDoneView,
                                        PasswordResetConfirmView,
                                        PasswordResetCompleteView,
                                        PasswordChangeView,
                                        PasswordChangeDoneView,
                                        )

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home, name='home'),
    path('', BoardListView.as_view(), name='home'),
    # path('boards/<int:pk>/', board_topics, name='board_topics'),
    path('boards/<int:pk>/', TopicListView.as_view(), name='board_topics'),
    path('boards/<int:pk>/new/', new_topic, name='new_topic'),
    path('signup/', signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('reset/', PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt',
        ),
        name='password_reset'),
    path('reset/done/',
        PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('reset/complete/',
        PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    path('settings/password/', 
        PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    path('settings/password/done/',
        PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),
    path('settings/account/', UserUpdateView.as_view(), name='my_account'),
    # path('boards/<pk>/topics/<topic_pk>/', topic_posts, name='topic_posts'),
    path('boards/<pk>/topics/<topic_pk>/', PostListView.as_view(), name='topic_posts'),
    path('boards/<pk>/topics/<topic_pk>/reply/', reply_topic , name='reply_topic'),
    path('boards/<pk>/topics/<topic_pk>/posts/<post_pk>/edit/', PostUpdateView.as_view(), name='edit_post'),
]
