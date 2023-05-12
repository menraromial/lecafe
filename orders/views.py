from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Order,PaymentMethod
from .forms import OrderCreateForm
from cart.cart import Cart
from app.models import Item
from app.sending_mail import envoyer_mail_html
from django.utils import timezone
from datetime import date, datetime
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

#import datetime


def order_create(request):
    cart = Cart(request)
    pm = PaymentMethod.objects.all()
    order=None
    if request.method == 'POST':
        #form = OrderCreateForm(request.POST)
        fullname=request.POST.get('fullname')
        table_number= request.POST.get('table_number')
        pm_id = request.POST.get('pm_id')
        paymentMethod = get_object_or_404(PaymentMethod, id=pm_id)
        if fullname and table_number :
            order = Order(fullname=fullname, table_number=table_number)
            order.save()
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            if paymentMethod:
                order.paymentMethod=paymentMethod
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
            # set the order in the session
            request.session['order_id'] = order.id
            envoyer_mail_html(['menraromial@gmail.com'], 'Order success', {'order':order}, 'email/order-success.html')
        return render(request,'invoice/invoice.html', {'order':order})
    
    else:
        form=OrderCreateForm()
        context ={
            'cart':cart,
            'form':form,
            'pm':pm
        }
    return render(request, 'orders/create.html',context)

@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,'admin/orders/order/detail.html',{'order': order})

def cuisinier_page(request):
    # Récupérer la date d'aujourd'hui
    today = date.today()

    # Récupérer toutes les commandes créées aujourd'hui
    orders_today = Order.objects.filter(created__gte=timezone.make_aware(datetime.combine(today, datetime.min.time())))

    return render(request, 'orders/c_dasboard.html', {'orders':orders_today})

def cordon_page(request):
    # Récupérer la date d'aujourd'hui
    today = date.today()

    # Récupérer toutes les commandes créées aujourd'hui
    orders_today = Order.objects.filter(created__gte=timezone.make_aware(datetime.combine(today, datetime.min.time())))
    return render(request, 'orders/cb_dasboard.html', {'orders':orders_today})

def order_details(request):
    order_id = request.GET['id']
    order = get_object_or_404(Order, id=order_id)

    context =render_to_string('async/order-details.html', {'order': order})

    return JsonResponse({'data':context})

def update_order(request):
    if request.method == 'POST':
        order_id = request.POST['index']
        order = Order.objects.get(id=order_id)
        if order is None:
            return JsonResponse({'data':'error'})
        order.valide = True
        order.save()
        return JsonResponse({'data':'Ok'})

    return JsonResponse({'data':'error'})

@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    #template = get_template('admin/orders/order/pdf.html')
    context={'order':order}

    return render(request,'admin/orders/order/pdf.html', context )