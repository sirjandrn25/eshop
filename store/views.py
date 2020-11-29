from django.shortcuts import render,HttpResponse,redirect
from .forms import SignUpForm
from django.contrib.auth.hashers import check_password
from .models.customers import Customer
from django.contrib import messages
from .models.product import Product
from .models.category import Category
from .models.order import Order
from django.views import View
from .decorator import check_login

# Create your views here.
@check_login("/store/")
def login(request):
    flag = None
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            customer = Customer.objects.get(email=email)
        except:
            messages.error(request,"This email Address is not Valid")
            return redirect('/store/login')
        flag = check_password(password,customer.password)
        if flag:
            request.session['customer_id'] = customer.id
            return redirect('/store/')
        else:
            messages.error(request,'Password is not valid')
            return redirect('/store/login')
    
    
    return render(request,'store/login.html')
    


@check_login("/store/")
def signUp(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            customer = form.save()
            customer.hash_password()
            return HttpResponse('User successfully register')
    return render(request,'store/signup.html',{'form':form})

def logout(request):
    try:
        request.session['customer_id']
    except:
        messages.error(request,"User First Login")
        return redirect("/store/login")
    del request.session['customer_id']
    messages.success(request,'user successfully logout')
    return redirect('/store/login')



class Index(View):
    def post(self,request):
        product_id = request.POST.get('product_id')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        print(remove)
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                if remove:
                    cart[product_id] -=1
                    if cart[product_id] == 0:
                        del cart[product_id]
                else:
                    cart[product_id] +=1
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1
        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('home')
    def get(self,request):
        # print('Get request')
        try:
            cart = request.session['cart']
        except:
            request.session['cart'] = {}
        
        products = Product.objects.all()
        category = Category.objects.all()
        return render(request,'store/index.html',{'product':products,'category':category})


def category_filter(request,category_id):
    c = Category.objects.get(id = category_id)
    products = Product.objects.filter(category = c)
    category = Category.objects.all()
    return render(request,'store/index.html',{'product':products,'category':category})


def Cart(request):
    ids = list(request.session['cart'].keys())
    products = Product.get_products_by_id(ids)
    print(products)
    return render(request,"store/cart.html",{'products':products})

def CheckOut(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        phone_no = request.POST.get('phone_no')
        customer_id = request.session['customer_id']
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address,phone_no,customer_id,products)
        customer = Customer.objects.get(id = customer_id)
        print(cart.keys())
        for product in products:
            order = Order(customer = customer,
            product=product,quantity = cart.get(str(product.id)),
            price = product.price,address =address,
            phone=phone_no)
            order.save()
        
        request.session['cart'] = {}
        
        return redirect('cart')

def show_order(request):
    customer_id = request.session['customer_id']
    customer = Customer.objects.get(id=customer_id)
    orders = Order.order_get_by_customer(customer)
    orders = reversed(orders)
    print(orders)
    return render(request,"store/order.html",{'orders':orders})