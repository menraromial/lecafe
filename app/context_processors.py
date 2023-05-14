from app.models import Categorie
from django.db.models import Count

def category(request):
    categories = Categorie.objects.all()
    menus = Categorie.objects.annotate(nb_produits=Count('items')).filter(nb_produits__gt=0).order_by('-nb_produits')
    session_order_id=None
    #if request.session['order_id']:
    session_order_id = request.session.get('order_id', None)
    #produits = catégorie.produit_set.all()

    return {'categories':categories, 'menus':menus, 'session_order_id':session_order_id }