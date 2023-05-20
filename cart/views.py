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
    ids = request.POST.getlist('ids[]')
    #print('ingredient ids', ids)
    if quantity:
        cart.add(item=item,quantity=quantity,ids=ids, override_quantity=override_quantity)
        #print(cart.get_total_price())
    #cart.get_total_item_price(item_id)
    #print(cart.get_total_price())
    item_t_price=cart.get_total_item_price(item_id)
    context=render_to_string('async/cart-list.html',{'cart':cart})
    total_price = render_to_string('async/total_price.html',{'cart':cart})
    return JsonResponse({
        'data':context, 
        'total_items':len(cart),
        'total_price':total_price,
        'item_t_price':item_t_price
        })

#@require_POST
def cart_remove(request):
    item_id = request.GET['id']
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.remove(item)

    context=render_to_string('async/cart-list.html',{'cart':cart})
    total_price = render_to_string('async/total_price.html',{'cart':cart})
    get_total_price = cart.get_total_price()
    return JsonResponse({
        'cart_list':context,
        'total_price':total_price, 
        'total_items':len(cart),
        'get_total_price':get_total_price
        })

def cart_details(request):
    cart=Cart(request)
    coupon_apply_form = CouponApplyForm()
    context={
        'cart':cart,
        'coupon_apply_form':coupon_apply_form
    }
    return render(request, 'cart/shop-cart.html',context )
