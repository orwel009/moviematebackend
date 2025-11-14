from django.urls import path
from .views import signup_view, LoginView, me_view

urlpatterns = [
    path('auth/signup/', signup_view, name='auth-signup'),
    path('auth/login/', LoginView.as_view(), name='auth-login'),
    path('auth/me/', me_view, name='auth-me'),
]