from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Contact



class ContactForms(ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "subject", "body")
        widgets = {
            "name": TextInput(attrs={"class":"form-control", "placeholder":"Your Name", "id":"name"}),
            "email": EmailInput(attrs={"class":"form-control", "placeholder":"Your Email", "id":"email"}),
            "subject": TextInput(attrs={"class":"form-control", "placeholder":"Subject", "id":"subject"}),
            "body": Textarea(attrs={"class":"form-control", "placeholder":"Message", "id":"message", "rows":8}),
        }