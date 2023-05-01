from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from authuser.models import User
import os

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
        return reverse("detail_categorie", kwargs={"slug": self.slug})
    
    #def save(self, *args, **kwargs):  # new
    #    if not self.slug:
    #        self.slug = slugify(self.nom + '-' +self.id)
    #    return super().save(*args, **kwargs)

class Ingredient(models.Model):
    nom = models.CharField(max_length=256)
    cout = models.DecimalField(max_digits=999999999,decimal_places=2)
    ancien_cout = models.DecimalField(max_digits=999999999,decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=get_image_path)
    
    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("detail_ingredient", kwargs={"slug": self.slug})
    
    def get_image(self): #new
        return mark_safe(f'<img src = "{self.image.url}" height="50" width = "50"/>')

class Item(models.Model):
    title = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    ancien_cout = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField(blank=True, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=get_image_path)
    slug = models.SlugField(unique=True,null=False)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['title']),
            models.Index(fields=['-created']),]
            
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("detail_item", kwargs={"slug": self.slug})

    def get_image(self): #new
        return mark_safe(f'<img src = "{self.image.url}" height="50" width = "50"/>')
    
    def get_percentage(self):
        return (self.price/self.ancien_cout)*100

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.nom + ' ' + self.price)
        return super().save(*args, **kwargs)

class ItemImages(models.Model):
    images = models.ImageField(upload_to=get_image_path, default='item.png')
    item = models.ForeignKey(Item, on_delete=models.SET_NULL,null=True)
    class Meta:
        verbose_name_plural="Item Images"
class ItemIngredients(models.Model):
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    Ingredient=models.ForeignKey(Ingredient, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name_plural="Item Ingredients"
class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #items = models.ManyToManyField(Item)
    etat = models.CharField(max_length=100, choices=STATUT_COMMANDE)
    numero_table = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Commande"
        verbose_name_plural="Commandes"

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

    class Meta:
        verbose_name_plural="Cart Order Items"

    def get_image(self): #new
        return mark_safe(f'<img src = "/media/{self.image}" height="50" width = "50"/>')


class ItemReview(models.Model):
    item=models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.SmallIntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Item Reviews"
    
    def __str__(self):
        return self.item.nom
    
    def get_ratin(self):
        return self.rating