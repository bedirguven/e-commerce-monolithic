from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
]