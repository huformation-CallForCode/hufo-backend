from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]
    
if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(
            title='Hufo CallForCode API',
            default_version='v1',
            description='API documents for Huformation Team',
            license=openapi.License(name='MIT License'),
        ),
        public=True,
    )
    
    urlpatterns += [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
    ]   