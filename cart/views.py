from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from product.models import Product
from .cart_module import Cart
from .models import Order, OrderItem
from django.contrib.auth.mixins import LoginRequiredMixin

class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, "cart/cart_detail.html", {'Cart': cart})


class CartAddView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        size, color, quantity = request.POST.get("size", 'size'), request.POST.get("color", 'color'), request.POST.get("quantity")
        cart = Cart(request)
        cart.add(product, quantity, color, size)
        return redirect("cart:cart_detail")

class CartDeleteView(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.remove(id)
        return redirect("cart:cart_detail")


class OrderDetailView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        return render(request, 'cart/order_detail.html', {'order': order})
class OrderCreationView(View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user, total_price=cart.total())
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], color=item['color'], size=item['size'],
                                     quantity=item['quantity'], price=item['price'])
            return redirect('cart:order_detail', order.id)
