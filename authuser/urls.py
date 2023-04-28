from django.urls import path,include
from . import views

app_name="authuser"

urlpatterns = [
    path("sign-up", views.register_view, name="register"),
    path("sign-in", views.login_page, name="login"),
    path("sign-out", views.logout_view, name="logout")
]