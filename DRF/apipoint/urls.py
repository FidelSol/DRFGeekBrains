from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

# router
router.register(r'users', views.UserViewSet, basename='users')

from rest_framework.authtoken import views

urlpatterns = [
    # API
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token)
]
