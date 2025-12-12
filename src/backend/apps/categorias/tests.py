from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Categoria

User = get_user_model()

class CategoriaTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_user(
            email='admin@test.com', 
            password='testpass', 
            rol='admin',
            nombre='Admin User',
            is_staff=True
        )
        self.user = User.objects.create_user(
            email='user@test.com', 
            password='testpass', 
            rol='cliente',
            nombre='Test User'
        )
        self.categoria = Categoria.objects.create(
            nombre='Test Category',
            slug='test-category',
            descripcion='Test Description'
        )

    def test_get_categorias(self):
        response = self.client.get('/api/categorias/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_categoria_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        data = {'nombre': 'New Category', 'slug': 'new-category'}
        response = self.client.post('/api/categorias/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_categoria_user_forbidden(self):
        self.client.force_authenticate(user=self.user)
        data = {'nombre': 'New Category From User'}
        response = self.client.post('/api/categorias/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
