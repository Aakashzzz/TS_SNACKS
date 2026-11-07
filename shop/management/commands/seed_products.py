
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from shop.models import Product


PRODUCTS = [
    ("Bambe Mixture", "Mixture & Savouries", 170),
    ("AVL Mixture", "Mixture & Savouries", 170),
    ("Poondu Mixture", "Mixture & Savouries", 170),
    ("Kara Boondhi", "Mixture & Savouries", 170),
    ("Kerala Avara", "Traditional Snacks", 180),
    ("Ring Muruku", "Traditional Snacks", 170),
    ("Sevu", "Traditional Snacks", 180),
    ("Seval", "Traditional Snacks", 180),
    ("Rusk", "Bakery & Biscuits", 190),
    ("Ooty Varky (Special)", "Bakery & Biscuits", 200),
    ("Ooty Varky (Normal)", "Bakery & Biscuits", 180),
    ("Tomato Chips", "Chips & Snacks", 190),
    ("Pacha Pattani", "Chips & Snacks", 185),
    ("Uppu Kallai", "Chips & Snacks", 200),
    ("Masala Kallai", "Chips & Snacks", 250),
    ("Maravalli (Kucchi - Circle)", "Chips & Snacks", 250),
    ("Potato Chilli", "Chips & Snacks", 250),
    ("Potato Chips", "Chips & Snacks", 350),
    ("ABCD Biscuit", "Bakery & Biscuits", 200),
    ("Heart Biscuit", "Bakery & Biscuits", 200),
    ("Mundhiri Biscuit", "Bakery & Biscuits", 200),
    ("Muttai Biscuit", "Bakery & Biscuits", 200),
]


class Command(BaseCommand):
    help = "Add the TS Snacks product catalogue"

    def handle(self, *args, **options):
        for name, category, price in PRODUCTS:
            Product.objects.update_or_create(
                name=name,
                defaults={
                    "slug": slugify(name),
                    "category": category,
                    "price_per_kg": price,
                    "description": (
                        f"{name}, available from TS Snacks."
                    ),
                    "is_available": True,
                    "is_featured": name in [
                        "Bambe Mixture",
                        "Ooty Varky (Special)",
                        "Potato Chips",
                        "Poondu Mixture",
                    ],
                },
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Loaded {len(PRODUCTS)} TS Snacks products."
            )
        )
