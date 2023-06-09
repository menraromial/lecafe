from django.contrib import admin
from app.models import Categorie, Ingredient, Item, ItemImages, ItemReview,ItemIngredients


#@admin.register(ItemImages)
class ItemImagesAdmin(admin.TabularInline):
    model=ItemImages
class ItemIngredientsAdmin(admin.TabularInline):
    model=ItemIngredients

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImagesAdmin, ItemIngredientsAdmin]
    list_display=['title','get_image','price','available', 'created', 'updated']
    search_fields=['nom', 'description']
    list_filter=['categories', 'available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields={'slug':['title']}
    #filter(function, iterable)

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display=['nom','get_image', 'slug']
    prepopulated_fields={'slug':['nom']}

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display=['nom','cout']
    search_fields=['nom', 'description']

@admin.register(ItemReview)
class ItemReviewAdmin(admin.ModelAdmin):
    list_display=['fullname', 'rating', 'date']
'''
@admin.register(CartOrder)
class CartOrderAdmin(admin.ModelAdmin):
    list_display=['user', 'etat', 'numero_table','date']

@admin.register(CartOrderItems)
class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display=['get_image', 'qty','price']
'''