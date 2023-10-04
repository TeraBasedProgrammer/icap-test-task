from django.db.models import Q
from django.urls import reverse
from django.views import generic

from .forms import ProductModelForm
from .mixins import StaffRequiredMixin
from .models import Product


class ProductListView(StaffRequiredMixin, generic.ListView):
    model = Product
    template_name = 'admin_crud/products_list.html'
    context_object_name = 'products'

    paginate_by = 15


class ProductDetailView(StaffRequiredMixin, generic.DetailView):
    model = Product
    template_name = 'admin_crud/product_detail.html'
    context_object_name = 'product'


class ProductFilterView(StaffRequiredMixin, generic.ListView):
    context_object_name = 'products'
    template_name = 'admin_crud/products_list.html'

    paginate_by = 15

    def get_queryset(self):
        month_offer_filter = self.request.GET.get("month-offer")
        in_stock_filter = self.request.GET.get("in-stock")
        out_of_stock_filter = self.request.GET.get("out-of-stock")
        self_delivery_filter = self.request.GET.get("self-delivery")

        filter_query = Q()
        if month_offer_filter:
            filter_query &= Q(month_offer=True)
        if in_stock_filter:
            filter_query &= Q(in_stock=True)
        if out_of_stock_filter:
            filter_query &= Q(in_stock=False)
        if self_delivery_filter:
            filter_query &= Q(is_self_delivered=True)

        products = Product.objects.filter(
            filter_query
        )
            
        return products
    

class ProductSearchView(StaffRequiredMixin, generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'admin_crud/products_list.html'
    
    paginate_by = 15

    def get_queryset(self):
        query = self.request.GET.get("q")
        if not query:
            return Product.objects.all()

        object_list = Product.objects.filter(
            Q(title__icontains=query) 
        ).order_by('title', 'category')
        
        return object_list

    def get_success_url(self):
        return reverse("products:products-list")
    

class ProductCreateView(StaffRequiredMixin, generic.CreateView):
    template_name = "admin_crud/product_create.html"
    form_class = ProductModelForm
    
    def get_success_url(self):
        return reverse("products:products-list")


class ProductDeleteView(StaffRequiredMixin, generic.DeleteView):
    template_name = "admin_crud/product_delete.html"
    model = Product
    context_object_name = 'product'

    def get_success_url(self):
        return reverse("products:products-list")


class ProductUpdateView(StaffRequiredMixin, generic.UpdateView):
    template_name = "admin_crud/product_update.html"
    form_class = ProductModelForm
    model = Product
    context_object_name = 'product'

    def get_success_url(self):
        return reverse("products:products-list")