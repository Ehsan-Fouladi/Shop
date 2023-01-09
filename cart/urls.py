from . import views
from django.urls import path

app_name = "cart"
urlpatterns = [
    path("detail/", views.CartDetailView.as_view(), name="cart_detail"),
    path("add/", views.CartAddView.as_view(), name="cart_add"),
]