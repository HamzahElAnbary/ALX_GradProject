from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from .models import Order, OrderItem
from .forms import OrderForm
from rest_framework import generics, filters
from .serializers import RecipeSerializer, OrderSerializer
from django.db.models import Q

class RecipeListView(ListView):
    model = Recipe
    template_name = 'RestoBan/recipe_list.html'
    context_object_name = 'recipes'
    paginate_by = 10  # show 10 recipes per page

    def get_queryset(self):
        """
        Optionally filters recipes by a search query (`q`) in title or ingredients.
        """
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(ingredients__icontains=query)
            )
        return queryset.order_by('title')  # optional: order alphabetically

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'RestoBan/recipe_detail.html'
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

@login_required
def dashboard(request):
    return render(request, "dashboard.html")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def staff_required(view_func):
    """Helper decorator for staff-only views."""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper


@method_decorator(login_required, name='dispatch')
class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"
    context_object_name = "recipes"


@method_decorator(login_required, name='dispatch')
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"
    context_object_name = "recipe"


@method_decorator([login_required], name='dispatch')
class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipes/recipe_form.html"
    success_url = reverse_lazy("restoban:recipe_list")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def form_invalid(self, form):
        """Override to attach form to response for assertFormError."""
        response = super().form_invalid(form)
        response.context_data["form"] = form
        return response


@method_decorator([login_required], name='dispatch')
class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipes/recipe_form.html"
    success_url = reverse_lazy("restoban:recipe_list")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


@method_decorator([login_required], name='dispatch')
class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = "recipes/recipe_confirm_delete.html"
    success_url = reverse_lazy("restoban:recipe_list")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

# ---------------- Dashboard & Signup ---------------- #

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

# ---------------- Orders Views ---------------- #

@method_decorator(login_required, name='dispatch')
class OrderListView(ListView):
    model = Order
    template_name = "orders/order_list.html"
    context_object_name = "orders"

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(customer=user)


@method_decorator(login_required, name='dispatch')
class OrderDetailView(DetailView):
    model = Order
    template_name = "orders/order_detail.html"
    context_object_name = "order"

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(customer=user)


@method_decorator([login_required], name='dispatch')
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/order_form.html"
    success_url = reverse_lazy("restoban:order_list")

    def form_valid(self, form):
        if not self.request.user.is_staff:
            form.instance.customer = self.request.user
        return super().form_valid(form)


@method_decorator([login_required], name='dispatch')
class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/order_form.html"
    success_url = reverse_lazy("restoban:order_list")

    def dispatch(self, request, *args, **kwargs):
        order = self.get_object()
        if not request.user.is_staff and order.customer != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


@method_decorator([login_required], name='dispatch')
class OrderDeleteView(DeleteView):
    model = Order
    template_name = "orders/order_confirm_delete.html"
    success_url = reverse_lazy("restoban:order_list")

    def dispatch(self, request, *args, **kwargs):
        order = self.get_object()
        if not request.user.is_staff and order.customer != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class RecipeListAPI(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["title", "updated_at", "prep_time_minutes", "cook_time_minutes"]
    search_fields = ["title", "description", "ingredients"]

class RecipeDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class OrderListAPI(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["created_at", "status", "customer_name"]
    search_fields = ["customer_name"]

class OrderDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
