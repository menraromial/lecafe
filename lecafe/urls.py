
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls", namespace="app")),
    path("auth/", include("authuser.urls", namespace='authuser')),
    path('cart/', include('cart.urls',namespace='cart')),
    path('orders/', include('orders.urls',namespace='orders')),
    path('coupons/', include('coupons.urls', namespace='coupons')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('contacts/', include('contacts.urls', namespace='contacts')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
