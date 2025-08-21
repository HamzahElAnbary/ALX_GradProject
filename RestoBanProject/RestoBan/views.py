from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipe
from .forms import RecipeForm

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"
    context_object_name = "recipes"

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"
    context_object_name = "recipe"

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipes/recipe_form.html"
    success_url = reverse_lazy("restoban:recipe_list")

    def form_invalid(self, form):
        """Override to attach form to response for assertFormError."""
        response = super().form_invalid(form)
        response.context_data["form"] = form
        return response

class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipes/recipe_form.html"
    success_url = reverse_lazy("restoban:recipe_list")

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = "recipes/recipe_confirm_delete.html"
    success_url = reverse_lazy("restoban:recipe_list")
