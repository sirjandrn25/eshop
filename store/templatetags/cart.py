from django import template

register = template.Library()

@register.filter(name = 'is_in_cart')
def is_in_cart(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    
    return False

# register.filter('is_in_cart',is_in_cart)

@register.filter(name = 'cart_quantity')
def cart_quantity(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    
    return 0

@register.filter(name = 'total_price')
def total_price(product,cart):
    quantity = cart_quantity(product,cart)
    return quantity*product.price

@register.filter(name = 'total_cart_price')
def total_cart_price(products,cart):
    sum = 0
    for product in products:
        sum += total_price(product,cart)
    return sum

@register.filter(name = "total_quantity")
def total_quantity(products,cart):
    sum = 0
    for product in products:
        sum += cart_quantity(product,cart)
    return sum
