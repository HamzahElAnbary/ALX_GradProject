from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipe
from .forms import RecipeForm

class RecipeListView(ListView):
    model = Recipe
    template_name = "RestoBan/recipe_list.html"
    context_object_name = "recipes"
    paginate_by = 10

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "RestoBan/recipe_detail.html"
    context_object_name = "recipe"
    slug_field = "slug"

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "RestoBan/recipe_form.html"

class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "RestoBan/recipe_form.html"
    slug_field = "slug"

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = "RestoBan/recipe_confirm_delete.html"
    success_url = reverse_lazy("restoban:recipe_list")
    slug_field = "slug"
