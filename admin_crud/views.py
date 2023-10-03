from django.db.models import Q
from django.urls import reverse
from django.views import generic

from .models import Product


class ProductListView(generic.ListView):
    model = Product
    template_name = 'admin_crud/products_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'admin_crud/product_detail.html'
    context_object_name = 'product'


class ProductFilterView(generic.ListView):
    context_object_name = 'products'
    template_name = 'admin_crud/products_list.html'

    def get_queryset(self):
        month_offer_filter = self.request.GET.get("moth_offer")
        is_available_filter = self.request.GET.get("available")
        is_self_delivered_filter = self.request.GET.get("self_delivered")
        
                
        products = Product.objects.filter(
            Q(month_offer=month_offer_filter) 
            | Q(is_available=is_available_filter)
            | Q(is_self_delivered=is_self_delivered_filter)
        )
            
        return products
    

class ProductSearchView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'admin_crud/products_list.html'
    
    def get_queryset(self):
        query = self.request.GET.get("q")

        object_list = Product.objects.filter(
            Q(title__icontains=query) 
            | Q(category__icontains=query)
            ).order_by('title', 'category')
        
        return object_list
    

class ProductCreateView(generic.CreateView):
    template_name = "admin_crud/product_create.html"
    form_class = ...
    
    def get_success_url(self):
        return reverse("products:products-list")


class ProductDeleteView(generic.DeleteView):
    template_name = "admin_crud/product_delete.html"
    model = Product
    context_object_name = 'product'

    def get_success_url(self):
        return reverse("products:products-list")


class ProductUpdateView(generic.UpdateView):
    template_name = "admin_crud/product_update.html"
    form_class = ...
    model = Product
    context_object_name = 'product'

    def get_success_url(self):
        return reverse("products:products-list")