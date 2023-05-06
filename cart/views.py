from django.shortcuts import render, redirect,get_object_or_404
from django.views.decorators.http import require_POST
from app.models import Item
from .cart import Cart
from coupons.forms import CouponApplyForm
from django.http import JsonResponse
from django.template.loader import render_to_string

@require_POST
def cart_add(request):
    item_id=request.POST.get('item-id')
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    quantity = int(request.POST.get('qty'))
    override_quantity = int(request.POST.get('oqty'))
    if quantity:
        cart.add(item=item,quantity=quantity, override_quantity=override_quantity)
    context=render_to_string('async/cart-list.html',{'cart':cart})
    return JsonResponse({'data':context, 'total_items':len(cart)})

#@require_POST
def cart_remove(request):
    item_id = request.GET['id']
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.remove(item)

    context=render_to_string('async/cart-list.html',{'cart':cart})
    return JsonResponse({'data':context, 'total_items':len(cart)})

def cart_details(request):
    cart=Cart(request)
    coupon_apply_form = CouponApplyForm()
    context={
        'cart':cart,
        'coupon_apply_form':coupon_apply_form
    }
    return render(request, 'cart/shop-cart.html',context )
