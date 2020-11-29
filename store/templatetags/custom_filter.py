from django import template

register = template.Library()

@register.filter(name = 'currency')
def currency(price):
    return "Rs. "+str(price)

@register.filter(name = 'multipy')
def multipy(quantity,price):
    return quantity*price
