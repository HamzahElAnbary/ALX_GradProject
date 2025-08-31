from django.urls import path
from .views import (
    RecipeListAPI,
    RecipeDetailAPI,
    OrderListAPI,
    OrderDetailAPI,
)

app_name = "api"

urlpatterns = [
    path("recipes/", RecipeListAPI.as_view(), name="recipe_list_api"),
    path("recipes/<int:pk>/", RecipeDetailAPI.as_view(), name="recipe_detail_api"),
    path("orders/", OrderListAPI.as_view(), name="order_list_api"),
    path("orders/<int:pk>/", OrderDetailAPI.as_view(), name="order_detail_api"),
]
