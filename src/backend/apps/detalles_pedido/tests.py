from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from apps.productos.models import Pedido, Tienda, Producto, DetallePedido
from apps.detalles_pedido.models import Factura
from apps.categorias.models import Categoria

User = get_user_model()

class FacturaTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='client@test.com', password='pass', rol='cliente', nombre='Cliente')
        self.admin = User.objects.create_user(email='admin@test.com', password='pass', rol='admin', nombre='Admin', is_staff=True)
        self.tienda_admin = User.objects.create_user(email='store@test.com', password='pass', rol='admin', nombre='TiendaAdmin')
        self.proveedor = User.objects.create_user(email='prov@test.com', password='pass', rol='proveedor', nombre='Proveedor')

        self.tienda = Tienda.objects.create(nombre='Test Store', direccion='Test', administrador=self.tienda_admin)
        self.categoria = Categoria.objects.create(nombre='Test Cat', descripcion='Desc')
        self.producto = Producto.objects.create(
             nombre='Prod 1', descripcion='Desc', precio=100.00, stock=10, 
             tienda=self.tienda,
             proveedor=self.proveedor,
             categoria=self.categoria
        )

        self.pedido = Pedido.objects.create(cliente=self.user, tienda=self.tienda, estado='pendiente')
        # Add details to make total > 0. 
        # Note: DetallePedido save triggers pedido.calcular_total() -> pedido.save() -> signal -> Factura creation.
        DetallePedido.objects.create(pedido=self.pedido, producto=self.producto, cantidad=1, precio_unitario=100.00)
        
        # Reload pedido to get updated relations (factura)
        self.pedido.refresh_from_db()

    def test_factura_created_automatically(self):
        self.assertTrue(hasattr(self.pedido, 'factura'))
        self.assertEqual(self.pedido.factura.total, 100.00)
        self.assertEqual(self.pedido.factura.cliente, self.user)

    def test_get_facturas_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get('/api/facturas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_factura_detail_owner(self):
        self.client.force_authenticate(user=self.user)
        factura_id = self.pedido.factura.id
        response = self.client.get(f'/api/facturas/{factura_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], factura_id)
