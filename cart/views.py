from django.shortcuts import render, redirect,get_object_or_404
from django.views.decorators.http import require_POST
from app.models import Item
from .cart import Cart
from coupons.forms import CouponApplyForm

@require_POST
def cart_add(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    quantity = request.POST.get('qty')
    override_quantity = request.POST.get('oqty')
    if quantity:
        cart.add(item=item,quantity=quantity, override_quantity=override_quantity)
    
    return #A JSON

@require_POST
def cart_remove(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.remove(item)

    return #A json

def cart_details(request):
    cart=Cart(request)
    coupon_apply_form = CouponApplyForm()
    context={
        'cart':cart,
        'coupon_apply_form':coupon_apply_form
    }
    return render(request, 'cart/shop-cart.html',context )
