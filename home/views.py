from django.shortcuts import render
from django.views.generic import ListView
from product.models import Product
from django.db.models import Q
from django.core.paginator import Paginator


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
    paginate_by = 1
    ordering = ('-times',)

    def get_context_data(self, **kwargs):
        request = self.request
        colors = request.GET.getlist("color")
        sizes = request.GET.getlist("size")
        min_price = request.GET.get("min-price")
        max_price = request.GET.get("max-price")
        queryset = Product.objects.all()
        if colors:
            queryset = queryset.filter(color__title__in=colors).distinct()
        if sizes:
            queryset = queryset.filter(size__title__in=sizes).distinct()
        if min_price and max_price:
            queryset = queryset.filter(
                price__lte=max_price, price__gte=min_price)
        context = super(ListShopView, self).get_context_data(**kwargs)
        context["object_list"] = queryset
        return context


def SearchView(request):
    q = request.GET.get('q')
    products = Product.objects.filter(
        Q(title__icontains=q) | Q(description__icontains=q))
    page_number = request.GET.get('page')
    paginator = Paginator(products, 1)
    object_list = paginator.get_page(page_number)
    return render(request, 'home/list_Shop.html', {"object_list": object_list})
