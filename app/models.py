from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from authuser.models import User
import os
from django_resized import ResizedImageField
from taggit.managers import TaggableManager
#from PIL import Image

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
    description = models.TextField(null=True, blank=True)
    image = ResizedImageField(size = [400, 120],upload_to=get_image_path, null=True, default='cat.png')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("app:c-details", kwargs={"slug": self.slug})
        
    def get_image(self): #new
        return mark_safe(f'<img src = "{self.image.url}" height="50" width = "50"/>')
    

    
    #def save(self, *args, **kwargs):  # new
    #    if not self.slug:
    #        self.slug = slugify(self.nom + '-' +self.id)
    #    return super().save(*args, **kwargs)

class Ingredient(models.Model):
    nom = models.CharField(max_length=256)
    cout = models.DecimalField(max_digits=999999999,decimal_places=2)
    ancien_cout = models.DecimalField(max_digits=999999999,decimal_places=2)
    description = models.TextField(blank=True)
    image = ResizedImageField(size=[195, 196],upload_to=get_image_path)
    
    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("detail_ingredient", kwargs={"slug": self.slug})
    
    def get_image(self): #new
        return mark_safe(f'<img src = "{self.image.url}" height="50" width = "50"/>')

class Item(models.Model):
    title = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    #ancien_cout = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField(blank=True, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    image = ResizedImageField(size=[195, 196],upload_to=get_image_path)
    slug = models.SlugField(unique=True,null=False)
    available = models.BooleanField(default=True)
    tags = TaggableManager()
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
        return reverse("app:p-details", kwargs={"slug": self.slug})

    def get_image(self): #new
        return mark_safe(f'<img src = "{self.image.url}" height="50" width = "50"/>')
    
    def get_percentage(self):
        return (self.price/self.ancien_cout)*100


class ItemImages(models.Model):
    image = ResizedImageField(size=[410, 288],upload_to=get_image_path, default='item.png')
    item = models.ForeignKey(Item, on_delete=models.CASCADE,null=True, related_name='item_images')
    class Meta:
        verbose_name_plural="Item Images"
class ItemIngredients(models.Model):
    item=models.ForeignKey(Item, on_delete=models.CASCADE, related_name='ingredients')
    ingredient=models.ForeignKey(Ingredient, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name_plural="Item Ingredients"
    
    def __str__(self):
        return self.ingredient.nom




class ItemReview(models.Model):
    item=models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, related_name='item_review')
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