from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from product.models import Product


class HomeView(ListView):
    template_name = 'home/index.html'
    model = Product

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     self.request.session.get("my_name", "ADDCART")
    #     return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders"] = Product.objects.all().order_by("-times")
        return context

class ListShopView(ListView):
    template_name = "home/list_Shop.html"
    model = Product
    queryset = Product.objects.order_by("-times")