from django.urls import path
from . import views


name_app = 'product'
urlpatterns = [
    path('<int:pk>/', views.ProductDetailView.as_view(), name="detail"),
    path('categories/', views.NavbarView.as_view(), name='navbar'),
    path("contact/", views.ContactUserView.as_view(), name="contact"),
]