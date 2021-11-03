from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# router
router.register(r'presentprojects', views.PresentProjectViewSet, basename='presentprojects')
router.register(r'crudprojects', views.CRUDProjectViewSet, basename='crudprojects')
router.register(r'presenttodos', views.PresentToDoViewSet, basename='presenttodos')
router.register(r'crudtodos', views.CRUDToDoViewSet, basename='crudtodos')

urlpatterns = [
    # API
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
