from django.forms import ModelForm, ValidationError

from .models import Product
from .services import validate_image_url


class ProductModelForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_photo_url(self):
        photo_url = self.cleaned_data.get("photo_url")
        if not validate_image_url(photo_url):
            raise ValidationError("Image url is not valid")
        return photo_url
        