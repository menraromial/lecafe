from decimal import Decimal
from django.conf import settings

from app.models import Item,Ingredient
from coupons.models import Coupon

class Cart:
    def __init__(self,request):
        # Initialize the cart
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        # store current applied coupon
        self.coupon_id = self.session.get('coupon_id')
    # add item in the cart
    def add(self, item,ids,quantity=1,override_quantity=False):
        item_id = str(item.id)
        if item_id not in self.cart:
            ing_prices = Decimal(0)
            ing_names =[]
            if len(ids)>0:
                
                ingeredients = Ingredient.objects.filter(id__in=ids)
                ing_prices = sum(ing.cout for ing in ingeredients)
                ing_names = [ing.nom for ing in ingeredients]
                #ing_names = ','.join(names)

            self.cart[item_id] = {'quantity':0,'ingredients':ing_names, 'price':str(item.price+ing_prices)}
        if override_quantity:
            self.cart[item_id]['quantity'] = quantity
        else:
            self.cart[item_id]['quantity'] += quantity
        self.save()
    
    def save(self):
        self.session.modified = True
    
    def remove(self, item):
        item_id = str(item.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()
    
    def __iter__(self):
        #Iterate over the items in the cart and get the products from database.
        item_ids = self.cart.keys()
        #get the product objects and add them to the cart
        items = Item.objects.filter(id__in=item_ids)
        cart = self.cart.copy()
        for item in items:
            cart[str(item.id)]['item_image'] = item.image.url
            cart[str(item.id)]['item_title'] = item.title
            cart[str(item.id)]['id'] = item.id
        for item in cart.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price']*item['quantity']
            yield item
    
    def __len__(self):
        #Count all items in the cart
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())

    def get_total_item_price(self, id):
        #cart = self.cart.copy()
        return self.cart[str(id)]['quantity']*self.cart[str(id)]['price']

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()
    
    @property
    def coupon(self):
        if self.coupon_id:
            try:
                return Coupon.objects.get(id=self.coupon_id)
            except Coupon.DoesNotExist:
                pass
        return None
    
    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount/Decimal(100))*self.get_total_price()
        return Decimal(0)
    
    def get_total_price_after_discount(self):
        return self.get_total_price()-self.get_discount()
