from django.contrib import admin
from .models import Recipe, Order, OrderItem

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "servings", "prep_time_minutes", "cook_time_minutes", "created_at")
    search_fields = ("title", "description", "ingredients")
    list_filter = ("category", "created_at")
    prepopulated_fields = {"slug": ("title",)}


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "status", "created_at", "updated_at", "total_price")
    list_filter = ("status", "created_at")
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "recipe", "quantity")
