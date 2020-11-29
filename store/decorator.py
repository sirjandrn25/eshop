from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages,sessions



def check_login(url):
    def decorator(function):
        @wraps(function)
        def wrapper(request,*args,**kwargs):
            try:
                request.session['customer_id']
            except:
                return function(request,*args,**kwargs)
            return redirect(url)
        return wrapper
    return decorator