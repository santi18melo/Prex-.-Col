from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.views.static import serve
from django.views.generic.base import RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import os

from backend.views.metrics import metrics_view
from backend.views.maps import logistics_map_data

api_info = openapi.Info(
    title="PREXCOL API",
    default_version='v1',
    description="API documentation for PREXCOL",
    terms_of_service="https://www.example.com/terms/",
    contact=openapi.Contact(email="support@example.com"),
    license=openapi.License(name="BSD License"),
)

schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=[permissions.AllowAny],
)

def api_root(request):
    return render(request, 'index.html')

# Documentation path
DOCS_ROOT = str(settings.BASE_DIR.parent / 'docs' / '_build' / 'html')

def serve_docs(request):
    return serve(request, 'index.html', document_root=DOCS_ROOT)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    path('', api_root, name='api-root'),
    
    
    # Documentation - Only /api/docs/
    path('api/docs/', serve_docs),
    re_path(r'^api/docs/(?P<path>.*)$', serve, {'document_root': DOCS_ROOT}),
    # Observability & Maps
    path('metrics/', metrics_view, name='metrics'),
    path('maps/logistica/', logistics_map_data, name='logistics_map'),

    # Auth routes
    path('api/auth/', include('apps.usuarios.urls_auth')),
    # User resource routes
    path('api/', include('apps.usuarios.urls')),
    # Product routes
    path('api/productos/', include('apps.productos.urls')),
    # Sales routes
    path('api/ventas/', include('apps.ventas.urls')),
    # Payment routes
    path('api/pagos/', include('apps.pagos.urls')),
    # Notification routes
    path('api/', include('apps.notificaciones.urls')),
    # Category routes
    path('api/categorias/', include('apps.categorias.urls')),
    # Order Details (Invoices)
    path('api/', include('apps.detalles_pedido.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
