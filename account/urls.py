from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
    path('login/', views.UserLogin.as_view(), name="login"),
    path('register/login/', views.Register_Login_View.as_view(), name="register_login"),
    path('checkotp/', views.CzechOtpView.as_view(), name="check_otp"),
    path('logout/', views.user_logout, name='logout'),
    path("address", views.AddAddressView.as_view(), name="Address"),
]