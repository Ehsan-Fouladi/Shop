from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from product.models import Product
from .cart_module import Cart

class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, "cart/cart_detail.html", {'Cart': cart})


class CartAddView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        size, color, quantity = request.POST.get("size"), request.POST.get("color"), request.POST.get("quantity")
        cart = Cart(request)
        cart.add(product, quantity, color, size)
        return redirect("cart:cart_detail")

class CartDeleteView(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.remove()
        return redirect("cart:cart_detail")

