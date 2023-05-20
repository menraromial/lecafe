from django.urls import path, include
from . import views
from . import webhooks

app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('paypal/process/', views.paypal_process_payment, name="paypal_process"),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('completed/', views.payment_completed, name='completed'),
    path('canceled/', views.payment_canceled, name='canceled'),
    path('webhook/', webhooks.stripe_webhook, name='stripe-webhook'),
]