from django.views.generic import ListView, DetailView

from .models import Product

class ProductListView(ListView):
    paginate_by = 6
    model = Product
    object_context_name = 'product_list'
    template_name = 'sewing/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    object_context_name = 'product'
    template_name = 'sewing/product_detail.html'


