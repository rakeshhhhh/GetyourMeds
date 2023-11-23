from django.urls import path
from .views import *

urlpatterns = [
    path('',Home,name='shop_home'),
    path('all/stock/',AllStock,name='shop_all_stock'),
    path('manage/stock/',ManageStock,name='shop_manage_stock'),
    path('request/stock/',RequestStock,name='shop_request_stock'),
    path('del/stock/<id>',Delete,name='shop_delete_stock'),
    path('rerequest/',ReRequest,name='shop_rereq'),
    path('order/',Order,name='shop_order'),
    path('order/accept/<id>',OrderAccept,name='shop_order_accept'),
    path('order/history/',OrderHistory,name='shop_order_history'),
]