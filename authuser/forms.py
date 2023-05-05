from django.contrib.auth.forms import UserCreationForm
from authuser.models import User
from django import forms


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Nom d'utilisateur"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email"}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Téléphone"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Mot de passe"}))

    class Meta:
        model=User
        fields = ['username', 'email', 'telephone', 'password']