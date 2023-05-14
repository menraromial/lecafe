from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('admin/order/<int:order_id>/', views.admin_order_detail,name='admin_order_detail'),
    path('admin/order/<int:order_id>/pdf/',views.admin_order_pdf,name='admin_order_pdf'),
    path('details/', views.order_details, name="order_details"),
    path('update/', views.update_order, name='update_order'),
    path('serveur/dashboard', views.cuisinier_page, name="c_dasboard"),
    path('cordon-bleu/dashboard', views.cordon_page, name="cb_dasboard")
]