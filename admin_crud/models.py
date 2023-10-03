from decimal import Decimal

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator


class Product(models.Model):
    class Categories(models.TextChoices):
        CPU = "PR", _("Процесор")
        GRAPHICS_CARD = "GC", _("Відеокарта")
        KEYBOARD = "KB", _("Клавіатура")
        MOUSE = "MS", _("Миша")
        SSD = "SD", _("SSD")
        MOTHERBOARD = "MB", _("Материнська плата")

    title = models.CharField(max_length=150, unique=True)
    photo_url = models.URLField()
    category = models.CharField(
        max_length=2, 
        choices=Categories.choices,
    )
    month_offer = models.BooleanField()
    is_available = models.BooleanField()
    is_self_delivered = models.BooleanField()
    description = models.TextField()

    price = models.DecimalField(
        max_digits=11, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.01'))]
    )
