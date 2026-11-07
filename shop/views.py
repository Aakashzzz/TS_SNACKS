from django.shortcuts import render
from .models import Product


def home(request):
    featured_products = Product.objects.filter(
        is_available=True,
        is_featured=True,
    )
    return render(
        request,
        "shop/home.html",
        {"featured_products": featured_products},
    )


def products(request):
    items = Product.objects.filter(is_available=True)
    category = request.GET.get("category", "").strip()
    search = request.GET.get("q", "").strip()

    if category:
        items = items.filter(category=category)

    if search:
        items = items.filter(name__icontains=search)

    categories = (
        Product.objects.filter(is_available=True)
        .values_list("category", flat=True)
        .distinct()
        .order_by("category")
    )

    return render(
        request,
        "shop/products.html",
        {
            "products": items,
            "categories": categories,
            "selected_category": category,
            "search_query": search,
        },
    )


def contact(request):
    return render(request, "shop/contact.html")

# Create your views here.
