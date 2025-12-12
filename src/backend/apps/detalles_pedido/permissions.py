from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Permite acceso solo al dueño de la factura o administradores.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.rol == 'admin':
            return True
        return obj.cliente == request.user
