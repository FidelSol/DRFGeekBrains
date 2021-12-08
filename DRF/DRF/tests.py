import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DRF.settings")
import django
django.setup()

from mixer.backend.django import mixer
from django.contrib.auth.models import User
from ToDo.models import Project
from rest_framework import status
from rest_framework.test import APITestCase

class TestBookViewSet(APITestCase):

    def test_get_list(self):
        response = self.client.get('/todo/api/v1/crudprojects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        project = Project.objects.create(name='Project')
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = self.client.put(f'/todo/api/v1/crudprojects/{project.id}/', {'name': 'Project'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = project.objects.get(id=project.id)
        self.assertEqual(project.name, 'Project')




