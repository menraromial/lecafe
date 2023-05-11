from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Coupon
from .forms import CouponApplyForm
from django.http import JsonResponse
from django.template.loader import render_to_string

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
            
            if request.session['coupon_id']:
                context="exist"
            else:
                request.session['coupon_id'] = coupon.id
                context="apply"
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
            context="DoesNotExist"
    context="CodeDoesNotExist"

    return JsonResponse({'data':context}) #return a json
