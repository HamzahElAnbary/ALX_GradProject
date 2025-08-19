from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "ingredients",
            "instructions",
            "category",
            "prep_time_minutes",
            "cook_time_minutes",
            "servings",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
            "ingredients": forms.Textarea(attrs={"rows": 6, "placeholder": "e.g.\n200g flour\n2 eggs\n1 tsp salt"}),
            "instructions": forms.Textarea(attrs={"rows": 8}),
        }

    def clean_title(self):
        title = self.cleaned_data.get("title", "").strip()
        if not title:
            raise forms.ValidationError("Title is required.")
        return title

    def clean_ingredients(self):
        ing = self.cleaned_data.get("ingredients", "").strip()
        lines = [line.strip(" \t\r") for line in ing.splitlines() if line.strip()]
        if not lines:
            raise forms.ValidationError("At least one ingredient is required (one per line).")
        # normalize to one-per-line
        return "\n".join(lines)

    def clean_instructions(self):
        instr = self.cleaned_data.get("instructions", "").strip()
        if not instr:
            raise forms.ValidationError("Instructions are required.")
        return instr
