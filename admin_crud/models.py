from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    class Categories(models.TextChoices):
        CPU = "PR", _("Процесор")
        GRAPHICS_CARD = "GC", _("Відеокарта")
        KEYBOARD = "KB", _("Клавіатура")
        MOUSE = "MS", _("Миша")
        SSD = "SD", _("SSD")
        MOTHERBOARD = "MB", _("Материнська плата")

    title = models.CharField(max_length=150)
    photo = models.URLField()
    category = models.CharField(
        max_length=2, 
        choices=Categories.choices,
    )
    month_offer = models.BooleanField()
    is_available = models.BooleanField()
    is_self_delivered = models.BooleanField()
    description = models.TextField()

    price = models.DecimalField(max_digits=11, decimal_places=2)
