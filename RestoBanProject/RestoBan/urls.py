from django.urls import path
from . import views

app_name = "restoban"

urlpatterns = [
    path("recipes/", views.RecipeListView.as_view(), name="recipe_list"),
    path("recipes/create/", views.RecipeCreateView.as_view(), name="recipe_create"),
    path("recipes/<slug:slug>/update/", views.RecipeUpdateView.as_view(), name="recipe_update"),
    path("recipes/<slug:slug>/delete/", views.RecipeDeleteView.as_view(), name="recipe_delete"),
    path("recipes/<slug:slug>/", views.RecipeDetailView.as_view(), name="recipe_detail"),
    path('', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
]
