from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ("appetizer", "Appetizer"),
        ("main", "Main Course"),
        ("dessert", "Dessert"),
        ("drink", "Drink"),
        ("side", "Side"),
    ]

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField(blank=True)
    ingredients = models.TextField(help_text="One ingredient per line")
    instructions = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="main")
    prep_time_minutes = models.PositiveIntegerField()
    cook_time_minutes = models.PositiveIntegerField()
    servings = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["slug"])]

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:200]
            candidate = base
            i = 1
            while Recipe.objects.filter(slug=candidate).exists():
                i += 1
                candidate = f"{base}-{i}"[:220]
            self.slug = candidate
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def total_time_minutes(self):
        return (self.prep_time_minutes or 0) + (self.cook_time_minutes or 0)


class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_price(self):
        return sum(item.recipe.price * item.quantity for item in self.items.all())

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username} - {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.recipe.title}"
