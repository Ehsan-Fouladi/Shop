from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.views import View
from .forms import FormLogin, OtpLoginForm, CzechOtpForm, AddressCreationForm
import ghasedakpack
from random import randint
from .models import Otp, User
from django.utils.crypto import get_random_string
from uuid import uuid4


SMS = ghasedakpack.Ghasedak("beee4729b279b215bd79847db9fb83756ec7002da0ef4b2a458ac2f55fed188c")

class UserLogin(View):
    def get(self, request):
        form = FormLogin()
        return render(request, "account/login.html", {"form":form})

    def post(self, request):
        form = FormLogin(request.POST)
        if form.is_valid():
            cd =  form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home:home')
            else:
                form.add_error('phone and email', 'error password is valid not found')
        else:
            form.add_error("phone and email", 'not found')
        return render(request, "account/login.html", {"form":form})



class Register_Login_View(View):
    def get(self, request):
        form = OtpLoginForm()
        return render(request, "account/register.html", {"form":form})

    def post(self, request):
        form = OtpLoginForm(request.POST)
        if form.is_valid():
            cd =  form.cleaned_data
            rendercode = randint(1000,9999)
            SMS.verification({'receptor': cd["number"],'type': '1','template': 'nordpython','param1': rendercode})
            token = str(uuid4())
            Otp.objects.create(number=cd["number"], code=rendercode, token=token)
            print(Otp)
            return redirect(reverse("account:check_otp") + f'?token={token}')
        else:
            form.add_error("number", 'invalid phone')
        return render(request, "account/register.html", {"form":form})



class CzechOtpView(View):
    def get(self, request):
        form = CzechOtpForm()
        return render(request, "account/check_otp.html", {"form":form})

    def post(self, request):
        token = request.GET.get('token')
        form = CzechOtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code=cd["code"], token=token).exists():
                otp = Otp.objects.get(token=token)
                user, is_create = User.objects.get_or_create(number=otp.number)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                otp.delete()
                return redirect("home:home")

        else:
            form.add_error("number", 'invalid phone')
        return render(request, "account/check_otp.html", {"form": form})


class AddAddressView(View):
    def post(self, request):
        form = AddressCreationForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)
        return render(request, "account/add_address.html", {"form": form})
    def get(self, request):
        form = AddressCreationForm
        return render(request, "account/add_address.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect('home:home')
