from django.urls import path
from .views import *

urlpatterns = [
    path('',Home,name='admin_home'),
    path('manage/shop/',ManageShop,name='admin_manage_shop'),
    path('manage/dealer/',ManageDealer,name='admin_manage_dealer'),
    path('delete/<sec>/<id>',DeleteShop,name='admin_delete'),
    path('approve/<sec>/<id>',Approve,name='admin_approve'),
]