from django.urls import path
from . import views

app_name = "restoban"

urlpatterns = [
    path("", views.RecipeListView.as_view(), name="recipe_list"),
    path("recipes/new/", views.RecipeCreateView.as_view(), name="recipe_create"),
    path("recipes/<slug:slug>/", views.RecipeDetailView.as_view(), name="recipe_detail"),
    path("recipes/<slug:slug>/edit/", views.RecipeUpdateView.as_view(), name="recipe_update"),
    path("recipes/<slug:slug>/delete/", views.RecipeDeleteView.as_view(), name="recipe_delete"),
]
