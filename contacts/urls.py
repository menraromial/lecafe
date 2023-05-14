from django.urls import path
from . import views

app_name="contacts"

urlpatterns = [
    path('send/', views.send_message,name='contact_send'),
]