from django.urls import path,include
from . import views

app_name="app"

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact" ),
    path("about/", views.about_page, name="about" ),
    path("blogs/", views.blog_view, name="blogs"),
    path("menu/", views.menu_view, name='menu'),
    path('product-details/<slug:slug>', views.product_details, name='p-details'),
    path('category-details/<slug:slug>', views.category_view, name='c-details'),
    path('review/add/', views.add_review, name='add_review'),
]