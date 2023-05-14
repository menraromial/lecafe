from django.shortcuts import render
from .models import Categorie, Item, ItemReview
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.template.loader import render_to_string

def home(request):

    #Boissons
    #drinks = Item.objects.filter(categorie__nom__icontains="boissons")
    #Petit dejeuner
    #breakfasts = Item.o
    items = Item.objects.filter(available=True)
    context = {
        'items':items
    }
    return render(request, "pages/index.html", context)


def contact(request):

    return render(request, 'pages/contact.html')

def about_page(request):

    return render(request, 'pages/about.html')


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

    categorie = get_object_or_404(Categorie, slug=slug)

    context = {
        'categorie':categorie
    }

    return render(request, 'pages/category-product.html', context)

@require_POST
def add_review(request):
    fullname=request.POST['fullname']
    rating = int(request.POST['rating'])
    review=request.POST['review']
    item_id = request.POST['item_id']
    item = get_object_or_404(Item, id=item_id)
    itemReview = ItemReview(fullname=fullname,rating=rating, review=review, item=item )
    itemReview.save()
    context = render_to_string('async/comments-container.html', {'item':item})
    return JsonResponse({"data":context})

