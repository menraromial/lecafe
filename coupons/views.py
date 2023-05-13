from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Coupon
from .forms import CouponApplyForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from cart.cart import Cart

@require_POST
def coupon_apply(request):
    now = timezone.now()
    code =request.POST['code']
    context = None
    if code:
        #code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(
                code__iexact=code,
                valid_from__lte=now,
                valid_to__gte=now,
                active=True
            )
            
            
            request.session['coupon_id'] = coupon.id
            cart = Cart(request)
            context=render_to_string('async/total_price.html',{'cart':cart})
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
            context="DoesNotExist"
    #context="CodeDoesNotExist"

    return JsonResponse({'data':context}) #return a json
