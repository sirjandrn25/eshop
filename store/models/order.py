from django.db import models
from .product import Product
from .customers import Customer
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    date = models.DateField(default = datetime.datetime.today)
    address = models.CharField(max_length=100,default='',blank=True)
    phone = models.CharField(max_length=100,default='',blank=True)
    staus = models.BooleanField(default=False)

    def order_get_by_customer(customer):
        return Order.objects.filter(customer = customer).order_by('-date')