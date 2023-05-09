from app.models import Categorie
from django.db.models import Count

def category(request):
    categories = Categorie.objects.all()
    menus = Categorie.objects.annotate(nb_produits=Count('item')).filter(nb_produits__gt=0).order_by('-nb_produits')
    #produits = catégorie.produit_set.all()

    return {'categories':categories, 'menus':menus }