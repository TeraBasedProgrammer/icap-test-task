from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    class Categories(models.TextChoices):
        CPU = "PR", _("Processor")
        GRAPHICS_CARD = "GC", _("Graphics card")
        KEYBOARD = "KB", _("Keyboard")
        MOUSE = "MS", _("Mouse")
        SSD = "SD", _("SSD")
        MOTHERBOARD = "MB", _("Motherboard")

    title = models.CharField(max_length=150, unique=True)
    photo_url = models.URLField()
    category = models.CharField(
        max_length=2, 
        choices=Categories.choices,
    )
    month_offer = models.BooleanField()
    in_stock = models.BooleanField()
    is_self_delivered = models.BooleanField()
    description = models.TextField()

    price = models.DecimalField(
        max_digits=11, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.01'))]
    )
