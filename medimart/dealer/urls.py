from django.urls import path
from .views import *

urlpatterns = [
    path('',Home,name='dealer_home'),
    path('add/med/',CreateMedicine,name='dealer_add_medicine'),
    path('manage/med/',ManageMed,name='dealer_manage_medicine'),
    path('edit/med/<id>',UpMed,name='dealer_edit_medicine'),
    path('delete/med/<id>',DelMed,name='dealer_delete_medicine'),
    path('request/',RequestMed,name='dealer_request'),
    path('accept/<id>',RequestAcpt,name='dealer_accept'),
]