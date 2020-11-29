from django.contrib import admin
from .models.customers import Customer
from .models.product import Product
from .models.category import Category
from .models.order import Order

# Register your models here.

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone']

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']

# class AdminOrder(admin.ModelAdmin):


admin.site.register(Customer,AdminCustomer)


admin.site.register(Product,AdminProduct)

admin.site.register(Category)

admin.site.register(Order)