from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('cuisinier/dashboard', views.cuisinier_page, name="c_dasboard"),
    path('cordon-bleu/dashboard', views.cordon_page, name="cb_dasboard")
]