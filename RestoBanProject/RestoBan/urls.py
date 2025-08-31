from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from .api_views import RecipeViewSet, OrderViewSet

app_name = "restoban"

# Standard web views
urlpatterns = [
    # Homepage points to recipe list
    path("", views.RecipeListView.as_view(), name="recipe_list"),

    # Recipe URLs
    path("recipes/", views.RecipeListView.as_view(), name="recipe_list"),
    path("recipes/create/", views.RecipeCreateView.as_view(), name="recipe_create"),
    path("recipes/<slug:slug>/", views.RecipeDetailView.as_view(), name="recipe_detail"),
    path("recipes/<slug:slug>/update/", views.RecipeUpdateView.as_view(), name="recipe_update"),
    path("recipes/<slug:slug>/delete/", views.RecipeDeleteView.as_view(), name="recipe_delete"),

    # Order URLs
    path("orders/", views.OrderListView.as_view(), name="order_list"),
    path("orders/create/", views.OrderCreateView.as_view(), name="order_create"),
    path("orders/<int:pk>/", views.OrderDetailView.as_view(), name="order_detail"),
    path("orders/<int:pk>/update/", views.OrderUpdateView.as_view(), name="order_update"),
    path("orders/<int:pk>/delete/", views.OrderDeleteView.as_view(), name="order_delete"),

    # Auth URLs
    path("signup/", views.signup, name="signup"),
    path("dashboard/", views.dashboard, name="dashboard"),
]

# API router for DRF
router = DefaultRouter()
router.register(r"api/recipes", RecipeViewSet, basename="api-recipes")
router.register(r"api/orders", OrderViewSet, basename="api-orders")

# Include router URLs
urlpatterns += router.urls
