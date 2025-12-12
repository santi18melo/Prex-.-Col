from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Factura
from .serializers import FacturaSerializer
from .permissions import IsOwnerOrAdmin
from .tasks import generate_invoice_pdf_task

class FacturaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para ver y descargar facturas.
    """
    serializer_class = FacturaSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.rol == 'admin':
            return Factura.objects.all()
        return Factura.objects.filter(cliente=user)

    @action(detail=True, methods=['get'])
    def download_pdf(self, request, pk=None):
        factura = self.get_object()
        if not factura.archivo_pdf:
            # Trigger generation task async
            generate_invoice_pdf_task.delay(factura.id)
            return Response(
                {"detail": "PDF generation started. Please try again in a moment."},
                status=status.HTTP_202_ACCEPTED
            )
        
        # In a real scenario, you'd return the file or a signed URL
        # For this example, we return the path/url
        return Response({"url": factura.archivo_pdf.url})
