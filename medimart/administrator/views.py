from django.shortcuts import redirect, render
from guest.models import ShopTable,CommonTable

# Create your views here.

def Home(request):
    context = {}
    return render(request,'administrator/home.html',context)

def ManageShop(request):
    context = {}
    context['data'] = ShopTable.objects.all()
    return render(request, 'administrator/manage_shop.html', context)

def ManageDealer(request):
    context = {}
    context['data'] = CommonTable.objects.filter(user_type='dealer')
    return render(request, 'administrator/manage_dealer.html', context)

def DeleteShop(request,id,sec):
    shop = CommonTable.objects.get(id=id)
    shop.delete()
    return redirect('admin_manage_%s'%sec)

def Approve(request,id,sec):
    shop = CommonTable.objects.get(id=id)
    if shop.is_active:
        shop.is_active = 0
        shop.save()
    else:
        shop.is_active = 1
        shop.save()
    return redirect('admin_manage_%s'%sec)