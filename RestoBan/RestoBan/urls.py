from django.urls import path
from RestoBan.views import RecipeUpdateView  # full import path

urlpatterns = [
    path("recipes/<slug:slug>/edit/", RecipeUpdateView.as_view(), name="recipe_update"),
]
