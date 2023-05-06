from app.models import Categorie

def category(request):
    categories = Categorie.objects.all()

    return {'categories':categories }