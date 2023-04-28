from django.contrib.auth.forms import UserCreationForm
from authuser.models import User
from django import forms


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Nom d'utilisateur","class":"form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email", "class":"form-control"}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Téléphone","class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Mot de passe","class":"form-control"}))

    class Meta:
        model=User
        fields = ['username', 'email', 'telephone', 'password']