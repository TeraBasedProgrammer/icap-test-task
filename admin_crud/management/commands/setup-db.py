import json

from django.core.management.base import BaseCommand
from tqdm import tqdm

from admin_crud.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("admin_crud/management/commands/data.json", "r", encoding="utf-8") as file:
            data = json.loads(file.read())

        for product in tqdm(data, desc="Processing"):
            Product.objects.create(
                title=product["title"],
                photo_url=product["photo_url"],
                category=product["category"],
                month_offer=product["month_offer"],
                in_stock=product["in_stock"],
                is_self_delivered=product["is_self_delivered"],
                description=product["description"],
                price=product["price"],
            )
