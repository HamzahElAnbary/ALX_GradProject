from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "servings", "prep_time_minutes", "cook_time_minutes", "created_at")
    search_fields = ("title", "description", "ingredients")
    list_filter = ("category", "created_at")
    prepopulated_fields = {"slug": ("title",)}
