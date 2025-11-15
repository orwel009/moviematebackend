from django.urls import path, include
from rest_framework import routers
from .views import signup_view, LoginView, me_view, MovieViewSet, AdminMovieViewSet, add_from_admin_view

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movies')
router.register(r'admin-movies', AdminMovieViewSet, basename='admin-movies')

urlpatterns = [
    path('auth/signup/', signup_view, name='auth-signup'),
    path('auth/login/', LoginView.as_view(), name='auth-login'),
    path('auth/me/', me_view, name='auth-me'),
    path('movies/from-admin/<int:pk>/', add_from_admin_view, name='movies-from-admin'),

    path('', include(router.urls)),
]
