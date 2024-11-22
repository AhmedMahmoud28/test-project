from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("invoiceapp.urls")),
]

# swagger urls and configuration
schema_view = get_schema_view(
    openapi.Info(
        title="invoice API",
        default_version="v1",
        description="Swagger Documentation",
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
    authentication_classes=(SessionAuthentication,),
    patterns=urlpatterns,
)
urlpatterns += [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
