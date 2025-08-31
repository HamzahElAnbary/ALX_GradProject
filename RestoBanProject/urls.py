from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("RestoBan.api_urls")),  # your API routes
    path("api-auth/", include("rest_framework.urls")),  # DRF login
    path("", include("RestoBan.urls")),  # all app routes
]
