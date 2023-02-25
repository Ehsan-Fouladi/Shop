from django.views.decorators.cache import cache_page
from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', cache_page(60 * 1)(views.HomeView.as_view()), name='home')
]