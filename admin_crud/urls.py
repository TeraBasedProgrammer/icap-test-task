from django.urls import path

from .views import (ProductCreateView, ProductDeleteView, ProductDetailView,
                    ProductFilterView, ProductListView, ProductSearchView,
                    ProductUpdateView)

app_name = "products"

urlpatterns = [
    path("", ProductListView.as_view(), name="products-list"),
    path("filter/", ProductFilterView.as_view(), name="products-filter"),
    path("search/", ProductSearchView.as_view(), name="products-search"),
    path("create/", ProductCreateView.as_view(), name="product-create"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("<int:pk>/update/", ProductUpdateView.as_view(), name="product-update"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product-delete"),
]