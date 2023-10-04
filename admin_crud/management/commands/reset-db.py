from django.core.management.base import BaseCommand
from django.db.models import Model

from admin_crud.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        deleted_count, _ = Product.objects.all().delete()
        print(f"Succsessfully deleted {deleted_count} Product objects")
        
