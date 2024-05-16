from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import CarSerializer
from .models import Car

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    @action(methods=['post'], detail=True, url_path='add-depreciation-cost')
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['cost', 'date'],
        properties={
            'cost': openapi.Schema(type=openapi.TYPE_INTEGER),
            'date': openapi.Schema(type=openapi.FORMAT_DATE)
        }
    ), responses={200: openapi.Response(description='Depreciation cost added', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={'status': openapi.Schema(type=openapi.TYPE_BOOLEAN)}))})
    def add_depreciation_cost(self, request, pk=None):
        # logic to add depreciation cost
        # ...
        return Response({'status': True})