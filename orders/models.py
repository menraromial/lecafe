from django.db import models
from app.models import Item
from coupons.models import Coupon
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal


class PaymentMethod(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    identifiant = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

        
class Order(models.Model):
    fullname = models.CharField(max_length=50)
    #last_name = models.CharField(max_length=50)
    #email = models.EmailField()
    #address = models.CharField(max_length=250, default="Le Café")
    table_number = models.CharField(max_length=20, default="7500")
    #city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    valide = models.BooleanField(default=False)
    paymentMethod = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, related_name='orders',null=True, blank=True)
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    class Meta:
        ordering = ['-created']
        indexes = [
        models.Index(fields=['-created']),
        ]
    def __str__(self):
        return f'Order {self.id}'
    def get_total_cost(self):
        total_cost = self.get_total_cost_before_discount()
        return total_cost - self.get_discount()
    
    def get_total_cost_before_discount(self):
        return sum(item.get_cost() for item in self.items.all())
    
    def get_discount(self):
        total_cost = self.get_total_cost_before_discount()
        if self.discount:
            return total_cost*(self.discount/Decimal(100))
        return Decimal(0)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    item = models.ForeignKey(Item,related_name='order_items',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price*self.quantity


    