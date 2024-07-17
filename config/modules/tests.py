from rest_framework.test import APITestCase, APIClient
from users.models import User
from .models import Modules
from django.urls import reverse
from rest_framework import status


class ModulesTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test_email@test.com',
            password='1234',
        )
        self.modules = Modules.objects.create(
            title='Тест',
            description='Тестовое описание',
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_modules_list(self):
        response = self.client.get(reverse('modules:modules_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_modules_create(self):
        data = {'title': 'test_title', 'description': 'test_description'}
        response = self.client.post(reverse('modules:modules_create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_modules_retrieve(self):
        response = self.client.get(reverse('modules:modules_retrieve', kwargs={'pk': self.modules.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_modules_update(self):
        data = {'title': 'test_update_title', 'description': 'test_update_description'}
        response = self.client.patch(reverse('modules:modules_update', kwargs={'pk': self.modules.id}), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_modules_destroy(self):
        response = self.client.delete(reverse('modules:modules_destroy', kwargs={'pk': self.modules.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_modules_str(self):
        self.assertEqual(str(self.modules), 'Тест')


