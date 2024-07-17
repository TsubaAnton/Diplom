from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from users.models import User
from django.test import TestCase
from .serializers import UserCreateSerializer


class UsersTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test1email@test.com',
            password='1234',
            phone='1234567890',
            city='Test1',
            avatar=None,
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        user_data = {
            'email': 'test2email@test.com',
            'password': '5678',
            'phone': '0987654321',
            'city': 'Test2',
        }
        response = self.client.post(reverse('users:user_create'), data=user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_update(self):
        self.user.phone = '0987654321'
        self.user.save()
        self.assertEqual(self.user.phone, '0987654321')

        update_data = {'phone': '0987654321'}
        response = self.client.patch(reverse('users:user_update', kwargs={'pk': self.user.pk}), data=update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserSerializerTestCase(TestCase):
    def test_user_create(self):
        user_data = {
            'email': 'test@email.com',
            'password': 'testpassword123',
            'phone': '1234567890',
            'city': 'TestCity',
            'avatar': None
        }
        serializer = UserCreateSerializer(data=user_data)
        self.assertTrue(serializer.is_valid())

        user = serializer.create(validated_data=user_data)

        self.assertEqual(user.email, 'test@email.com')
        self.assertEqual(user.phone, '1234567890')
        self.assertEqual(user.city, 'TestCity')
        self.assertTrue(user.check_password(user_data['password']), "Password not set correctly.")
