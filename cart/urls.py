from . import views
from django.urls import path

app_name = "cart"
urlpatterns = [
    path("detail/", views.CartDetailView.as_view(), name="cart_detail"),
    path("add/<int:pk>", views.CartAddView.as_view(), name="cart_add"),
    path("remove/<str:id>", views.CartDeleteView.as_view(), name="cart_delete"),
    path("order/<int:pk>", views.OrderDetailView.as_view(), name='order_detail'),
    path("order/create", views.OrderCreationView.as_view(), name='order_create'),
    path("discount_code/<int:pk>", views.ApplyDiscountView.as_view(), name='discount_code'),
]