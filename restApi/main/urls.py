from django.urls import path, include
from .views import ClienteViewSet, AdvogadoViewSet, ProcessoViewSet
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'advogados', AdvogadoViewSet)
router.register(r'processos', ProcessoViewSet)

"""Dessa forma ai em cima o router do django ja vai criar as views [GET, POST, PUT, DELETE E PATCH]"""

urlpatterns = [
    path('', include(router.urls)),
]
