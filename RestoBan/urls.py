from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .api_views import RecipeViewSet, OrderViewSet

app_name = "restoban"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # homepage
    path('signup/', views.signup, name='signup'),

    path('recipes/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipes/create/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('recipes/<slug:slug>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/<slug:slug>/update/', views.RecipeUpdateView.as_view(), name='recipe_update'),
    path('recipes/<slug:slug>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),

    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('orders/create/', views.OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('orders/<int:pk>/update/', views.OrderUpdateView.as_view(), name='order_update'),
    path('orders/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order_delete'),
    
    # removed duplicate dashboard path
]

# API router
router = DefaultRouter()
router.register(r"api/recipes", RecipeViewSet, basename="api-recipes")
router.register(r"api/orders", OrderViewSet, basename="api-orders")
urlpatterns += router.urls
