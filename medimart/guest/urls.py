from django.urls import path
from .views import *

urlpatterns = [
    path('',Home,name='guest_home'),
    path('reg_customer/',Customer,name='guest_customer'),
    path('reg_dealer/',Dealer,name='guest_dealer'),
    path('reg_shop/',Shop,name='guest_shop'),
    path('login/',Login,name='guest_login'),
    path('logout/',Logout,name='logout'),
    path('view/product/<id>',ProductView,name='guest_product'),
    path('customer/cart/',Cart,name='guest_cart_view'),
    path('cart/remove/<id>',RemoveProduct,name='guest_cart_remove'),
    path('review/post/',PostReview,name='guest_post_review'),
    path('update/cart/qty',UpdateCart,name='update_cart'),
    path('myorders/',Orders,name='guest_myorde'),
]