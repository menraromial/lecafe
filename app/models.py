from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from authuser.models import User

STATUT_COMMANDE =(
    ('VALIDE', 'Plat servi'),
    ('EN_ATTENTE', 'En attente'),
    ('ANNULE', 'Commande annulée')
)

RATING = (
    (1, "★☆☆☆☆"),
    (2, "★★☆☆☆"),
    (3, "★★★☆☆"),
    (4, "★★★★☆"),
    (5, "★★★★★")
)

def get_image_path(instance, filename):
    return os.path.join('images', str(instance.__class__.__name__), filename)


class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("detail_item", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Ingredient(models.Model):
    nom = models.CharField(max_length=256)
    cout = models.DecimalField(max_digits=999999999,decimal_places=2)
    ancien_cout = models.DecimalField(max_digits=999999999,decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=get_image_path)
    
    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("detail_item", kwargs={"slug": self.slug})
    
    def get_image(self): #new
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')

class Item(models.Model):
    nom = models.CharField(max_length=256)
    cout = models.DecimalField(max_digits=999999999,decimal_places=2)
    ancien_cout = models.DecimalField(max_digits=999999999,decimal_places=2)
    description = models.TextField(blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    ingredients = models.ManyToManyField(Ingredient)
    image = models.ImageField(upload_to=get_image_path)
    slug = models.SlugField(unique=True,null=False)

    def __str__(self):
        return self.nom
    def get_absolute_url(self):
        return reverse("detail_item", kwargs={"slug": self.slug})

    def get_image(self): #new
        return mark_safe(f'<img src = "{self.image.url}" height="50" width = "50"/>')
    
    def get_percentage(self):
        return (self.cout/self.ancien_cout)*100

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #items = models.ManyToManyField(Item)
    etat = models.CharField(max_length=100, choices=STATUT_COMMANDE)
    numero_table = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "commandé par " + self.user.username
    
    
    '''def getMontant(self):
        sum = 0.0
        for item in self.items:
            sum+=item.cout
        return sum'''

class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=9999999, decimal_places=2, default="1.9")


