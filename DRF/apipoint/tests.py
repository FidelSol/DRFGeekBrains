
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import UserViewSet
from .models import CustomUser


class TestUSERViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/v1/users/')
        view = UserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/v1/users/', {'last_name': 'Пушкин', 'first_name': 'Александр'}, format='json')
        view = UserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/v1/users/', {'last_name': 'Пушкин', 'first_name': 'Александр'}, format='json')
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        force_authenticate(request, admin)
        view = UserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        another_user = mixer.blend(CustomUser)
        client = APIClient()
        response = client.get(f'/api/v1/users/{another_user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        user = mixer.blend(CustomUser, last_name='Достоевский', first_name='Фёдор')
        client = APIClient()
        response = client.put(f'/api/v1/users/{user.id}/', {'last_name': user.last_name, 'first_name': user.first_name})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        user = mixer.blend(CustomUser, last_name='Достоевский', first_name='Фёдор')
        client = APIClient()
        admin = CustomUser.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        client.login(username='admin', password='admin123456')
        response = client.put(f'/api/v1/users/{user.id}/', {'last_name': user.last_name, 'first_name': user.first_name})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        search_user = CustomUser.objects.get(id=user.id)
        self.assertEqual(search_user.first_name, 'Достоевский')
        self.assertEqual(search_user.last_name, 'Фёдор')
        client.logout()


