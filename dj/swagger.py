# from rest_framework.response import Response
# from rest_framework.views import APIView
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from rest_framework import permissions

# schema_view = get_schema_view(
#    openapi.Info(
#       title="My API",
#       default_version='v1',
#       description="My API documentation",
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )

# class SwaggerView(APIView):
#     def get(self, request):
#         return Response(schema_view)

from drf_yasg import openapi

info = openapi.Info(
    title="Your API Title",
    default_version='v1',
    description="Your API description",
    terms_of_service="https://example.com/terms/",
    contact=openapi.Contact(email="your_email@example.com"),
    license=openapi.License(name="MIT License"),
)
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="Your API description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

