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
    path('contents/', views.ContentListView.as_view(), name = 'contents'),
    path('content/<int:pk>/', views.ContentDetailView.as_view(), name = 'detail_content'),
    path('mypage/', views.mypage, name = 'mypage'),
    # path('create_review/', views.ReviewView.asView(), name = 'create_review'),
    # path('update/<int:pk>/', CommentUpdateView.as_view(), name='comment-update'),
    # path('delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
]