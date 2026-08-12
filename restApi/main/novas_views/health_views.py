from rest_framework.views import APIView
from django.http import JsonResponse
from .services import HealthService
from .permissions import HealthCheckApi

class HealthCheckView(APIView):

    permission_classes = [HealthCheckApi]

    def get(self, request):
        health_data = HealthService.check_system_health()
        status_code = 200 if health_data["is_healthy"] else 503
        return JsonResponse(health_data["data"], status=status_code)