from pathlib import Path
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tc_snacks.settings")
django.setup()

from django.conf import settings
from shop.models import Product

products_dir = Path(settings.MEDIA_ROOT) / "products"

image_map = {
    "ABCD Biscuit": "abcd-biscuit",
    "Heart Biscuit": "heart-biscuit",
    "Mundhiri Biscuit": "mundhiri-biscuit",
    "Muttai Biscuit": "muttai-biscuit",
    "Ooty Varky (Normal)": "ooty-varky-normal",
    "Ooty Varky (Special)": "ooty-varky-special",
    "Rusk": "rusk",
    "Maravalli (Kucchi - Circle)": "maravalli",
    "Masala Kallai": "masala-kallai",
    "Pacha Pattani": "pacha-pattani",
    "Potato Chilli": "potato-chilli",
    "Potato Chips": "potato-chips",
    "Tomato Chips": "tomato-chips",
    "Uppu Kallai": "uppu-kallai",
    "AVL Mixture": "avl-mixture",
    "Bambe Mixture": "bambe-mixture",
    "Kara Boondhi": "kara-boondhi",
    "Poondu Mixture": "poondu-mixture",
    "Kerala Vada": "kerala-avare",
    "Ring Muruku": "ring-muruku",
    "Seval": "seval",
    "Sevu": "sevu",
}

extensions = {".jpg", ".jpeg", ".png", ".webp"}

for name, stem in image_map.items():
    matches = [
        f for f in products_dir.iterdir()
        if f.is_file()
        and f.stem.lower() == stem.lower()
        and f.suffix.lower() in extensions
    ]

    if not matches:
        print(f"MISSING FILE: {name} ({stem})")
        continue

    product = Product.objects.filter(name=name).first()

    if product is None:
        print(f"MISSING PRODUCT: {name}")
        continue

    product.image.name = f"products/{matches[0].name}"
    product.save(update_fields=["image"])
    print(f"ASSIGNED: {name} -> {matches[0].name}")

print("\n--- Verification ---")
for product in Product.objects.all():
    print(product.name, "->", product.image.name or "NO IMAGE")
