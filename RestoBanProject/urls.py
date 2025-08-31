from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("RestoBan.api_urls")),  # API routes
    path("api-auth/", include("rest_framework.urls")),  # DRF auth
    path("", include("RestoBan.urls")),  # app routes (dashboard, recipes, orders)
]
