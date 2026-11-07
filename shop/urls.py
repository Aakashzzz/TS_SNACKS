from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.products, name="products"),
    path("contact/", views.contact, name="contact"),
]