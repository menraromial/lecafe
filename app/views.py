from django.shortcuts import render
from .models import Categorie, Item
from django.shortcuts import get_object_or_404

def home(request):

    return render(request, "pages/index.html")


def contact(request):

    return render(request, 'pages/contact.html')

def about_page(request):

    return render(request, 'pages/about.html')

def blog_view(request):

    return render(request, "qr_code/index.html")

def menu_view(request):

    items = Item.objects.all()
    context = {
        'items':items
    }

    return render(request, 'pages/menu.html', context)

def product_details(request, slug):

    item = get_object_or_404(Item, slug=slug)
    context ={
        'item':item
    }
    return render(request, 'pages/product-details.html', context)

def category_view(request, slug):

    category = get_object_or_404(Categorie, slug=slug)

    context = {
        'category':category
    }

    return render(request, 'pages/category-product.html', context)
