from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from app.models import Item
from django.utils import timezone
from datetime import date, datetime
from django.http import JsonResponse
from django.template.loader import render_to_string

#import datetime


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        #form = OrderCreateForm(request.POST)
        fullname=request.POST.get('fullname')
        table_number= request.POST.get('table_number')
        if fullname and table_number :
            order = Order(fullname=fullname, table_number=table_number)
            order.save()
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            #item_ids = cart.keys()
            #get the product objects and add them to the cart
            #items = Item.objects.filter(id__in=item_ids)
            for cart_item in cart:
                item=Item.objects.get(id=cart_item['id'])
                OrderItem.objects.create(order=order,
                                        item = item,
                                        price=cart_item['price'],
                                        quantity=cart_item['quantity'])
            # clear the cart
            cart.clear()
        return render(request,'invoice/invoice.html', {'order':order})
    
    else:
        form=OrderCreateForm()
        context ={
            'cart':cart,
            'form':form
        }
    return render(request, 'orders/create.html',context)

def cuisinier_page(request):
    # Récupérer la date d'aujourd'hui
    today = date.today()

    # Récupérer toutes les commandes créées aujourd'hui
    orders_today = Order.objects.filter(created__gte=timezone.make_aware(datetime.combine(today, datetime.min.time())))

    return render(request, 'orders/c_dasboard.html', {'orders':orders_today})

def cordon_page(request):
    return render(request, 'orders/cb_dasboard.html')

def order_details(request):
    order_id = request.GET['id']
    order = get_object_or_404(Order, id=order_id)

    context =render_to_string('async/order-details.html', {'order': order})

    return JsonResponse({'data':context})

def update_order(request):
    order_id = request.GET['id']
    order = Order.objects.get(id=order_id)
    order.valide = True
    order.save()

    return JsonResponse({'data':'Ok'})