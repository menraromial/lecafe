from decimal import Decimal
import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse,get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from orders.models import Order
# create the Stripe instance
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION
def payment_process(request):
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        success_url = request.build_absolute_uri(reverse('payment:completed'))
        cancel_url = request.build_absolute_uri(reverse('payment:canceled'))
        # Stripe checkout session data
        session_data = {
        'mode': 'payment',
        'client_reference_id': order.id,
        'success_url': success_url,
        'cancel_url': cancel_url,
        'line_items': []
        }

        # add order items to the Stripe checkout session
        for order_item in order.items.all():
            session_data['line_items'].append({
            'price_data': {
            'unit_amount': int(order_item.price * Decimal('1.0')),
            'currency': 'xaf',
            'product_data': {
            'name': order_item.item.title,
            },
            },
            'quantity': order_item.quantity,
            })
        # Stripe coupon
        if order.coupon:
            stripe_coupon = stripe.Coupon.create(
            name=order.coupon.code,
            percent_off=order.discount,
            duration='once')
            session_data['discounts'] = [{
            'coupon': stripe_coupon.id
            }]
        # create Stripe checkout session
        session = stripe.checkout.Session.create(**session_data)
        # redirect to Stripe payment form
        return redirect(session.url, code=303)

    else:
        return render(request, 'payment/process.html', locals())


def payment_completed(request):
    #order_id = request.session.get('order_id', None)
    #order = get_object_or_404(Order, id=order_id)
    return render(request, 'payment/completed.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html')



def paypal_process_payment(request):
    order_id = request.session.get('order_id',None)
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.get_total_cost().quantize(
            Decimal('.01')),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'XAF',
        'notify_url': 'http://{}{}'.format(host,reverse('payment:paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,reverse('payment:completed')),
        'cancel_return': 'http://{}{}'.format(host,reverse('payment:canceled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/paypal_process.html', {'order': order, 'form': form})