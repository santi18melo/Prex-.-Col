from django.apps import AppConfig

class DetallesPedidoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.detalles_pedido'

    def ready(self):
        import apps.detalles_pedido.signals
