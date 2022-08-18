from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(openapi.Info(title='Сервис уведомлений', default_version='v1',
                                           description='API, который реализует службы обмена сообщениями',
                                           license=openapi.License(name='.'),
                                           ),
                              public=True,
                              permission_classes=[permissions.AllowAny, ],
                              )

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger(^<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
