from rest_framework import permissions
from django.conf import settings

class IsSystemStaff(permissions.BasePermission):
    """
    Somente o Staff pode acessar views com essa permissão. 
        Staff: é um usuário com privilégios administrativos, 
        mas não necessariamente é um superusuário. 
        Ele pode acessar a maioria das funcionalidades 
        administrativas, mas não tem acesso a todas as 
        permissões que um superusuário teria.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_staff

    
class IsSystemAdmin(permissions.BasePermission):
    """
    Somente o SuperUser(ADMIN) pode acessar views com essa permissão.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_superuser
    

class OnlyAdminDELETE(permissions.BasePermission):
    """
    Permite acesso total para SuperUser(ADMIN) e acesso somente leitura para outros usuários autenticados.
    """
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return request.user and request.user.is_authenticated and request.user.is_superuser
        return request.user and request.user.is_authenticated
    
    
class HealthCheckApi(permissions.BasePermission):
    def has_permission(self, request, view):
        token = request.headers.get('Health-Api-Key')
        
        if token and token == getattr(settings, 'HEALTH_API_KEY', None):
            return True
        return False
        