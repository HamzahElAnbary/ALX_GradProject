from django.test import TestCase
from django.urls import reverse
from RestoBan.models import Recipe

class TestRecipe(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            title="Pancakes",
            ingredients="200g flour\n2 eggs\n1 tsp salt",
            instructions="Mix and cook.",
            prep_time_minutes=10,
            cook_time_minutes=5,
            servings=2,
        )

    def test_list_page_loads(self):
        resp = self.client.get(reverse("restoban:recipe_list"))
        self.assertEqual(resp.status_code, 200)

    def test_detail_page(self):
        resp = self.client.get(reverse("restoban:recipe_detail", args=[self.recipe.slug]))
        self.assertContains(resp, "Pancakes")

    def test_create_validation(self):
        resp = self.client.post(reverse("restoban:recipe_create"), data={
            "title": "",
            "ingredients": "",
            "instructions": "",
            "prep_time_minutes": 0,
            "cook_time_minutes": 0,
            "servings": 0,
        })
        self.assertEqual(resp.status_code, 200)
        self.assertFormError(resp.context["form"], "title", "This field is required.")
        self.assertFormError(resp.context["form"], "ingredients", "This field is required.")
        self.assertFormError(resp.context["form"], "instructions", "This field is required.")
