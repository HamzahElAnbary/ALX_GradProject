from django.db import models
from django.utils.text import slugify

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ("appetizer", "Appetizer"),
        ("main", "Main Course"),
        ("dessert", "Dessert"),
        ("drink", "Drink"),
        ("side", "Side"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField(blank=True)
    # Store ingredients as one-per-line; you can normalize later into a related table
    ingredients = models.TextField(help_text="One ingredient per line")
    instructions = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="main")
    prep_time_minutes = models.PositiveIntegerField()
    cook_time_minutes = models.PositiveIntegerField()
    servings = models.PositiveIntegerField(default=1)
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
