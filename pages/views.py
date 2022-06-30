from django.views.generic import TemplateView, ListView
from sewing.models import Product

class HomePageView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'product_list'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(category='dog')


class AboutPageView(TemplateView):
    template_name = 'about.html'