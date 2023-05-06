from django.urls import path
from . import views

app_name="cart"

urlpatterns = [
    path('', views.cart_details,name='cart_detail'),
    path('add/', views.cart_add, name="cart_add"),
    path('remove/', views.cart_remove, name='cart_remove')
]