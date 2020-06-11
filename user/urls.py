from django.urls import path, include
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('create/', views.UserRegistrationView.as_view(), name = 'signup'),
    path('login/', views.UserLoginView.as_view(), name = 'login'),
    path('main/', views.main, name = 'index'),
    path('<pk>/verify/<token>/', views.UserVerificationView.as_view()),
    path('resend_verify_email/', views.ResendVerifyEmailView.as_view()),
    path('email_resent/', views.email_resend_page, name='email_resend'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
]