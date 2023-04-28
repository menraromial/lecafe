from django.contrib import admin
from import_export import resources
from app.models import Categorie, Ingredient, Item, ItemImages, ItemReview, CartOrder, CartOrderItems


#@admin.register(ItemImages)
class ItemImagesAdmin(admin.TabularInline):
    model=ItemImages

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImagesAdmin]
    list_display=['nom','get_image','cout','categorie']
    search_fields=['nom', 'description']
    list_filter=['categorie']
    prepopulated_fields={'slug':['nom','cout']}
    #filter(function, iterable)

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display=['nom', 'slug']
    prepopulated_fields={'slug':['nom']}

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display=['nom', 'get_image','cout']
    search_fields=['nom', 'description']

@admin.register(ItemReview)
class ItemReviewAdmin(admin.ModelAdmin):
    list_display=['user', 'rating', 'date']

