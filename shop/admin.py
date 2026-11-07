from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price_per_kg",
        "is_available",
        "is_featured",
    )
    list_filter = ("category", "is_available", "is_featured")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    
# Register your models here.
