from django.urls import path
from .views import signUp,login,logout,Index,category_filter,Cart,CheckOut,show_order
# from django.conf.urls.static import static
# from django.conf import settings


urlpatterns = [
    path('',Index.as_view(),name = 'home'),
    path('<int:category_id>/category_filter',category_filter,name = 'category_filter'),
    path('signup',signUp,name = 'signup'),
    path('login',login,name = 'login'),
    path('logout',logout,name = 'logout'),
    path('cart',Cart,name = "cart"),
    path('check_out',CheckOut,name = 'checkout'),
    path('order',show_order,name = 'order'),
    # path('profile',profile,name = 'profile'),
]
