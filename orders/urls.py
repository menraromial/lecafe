from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('details/', views.order_details, name="order_details"),
    path('update/', views.order_details, name='update_order'),
    path('cuisinier/dashboard', views.cuisinier_page, name="c_dasboard"),
    path('cordon-bleu/dashboard', views.cordon_page, name="cb_dasboard")
]