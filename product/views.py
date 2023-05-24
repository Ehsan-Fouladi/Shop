from django.views.generic import DetailView, TemplateView, FormView
from django.urls import reverse_lazy
from .models import Product, Category, Contact
from .forms import ContactForms

class ProductDetailView(DetailView):
    template_name = "product/detail.html"
    model = Product

class NavbarView(TemplateView):
    template_name = "include/navbar.html"

    def get_context_data(self, **kwargs):
        context = super(NavbarView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context
    

class ContactUserView(FormView):
    template_name = "product/contact.html"
    form_class = ContactForms
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)