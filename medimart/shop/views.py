from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from dealer.models import MedicineTable
from .models import *

# Create your views here.
def Home(request):
    context = {}
    return render(request,'shop/home.html',context)

def AllStock(request):
    if request.method == 'GET':
        context = {}
        context['data'] = MedicineTable.objects.filter(status='available')
        return render(request, 'shop/allstock.html', context)
    elif request.method == 'POST':
        medid = request.POST['medid']
        qty = request.POST['qty']
        if medid != None and qty != None:
            # e = RequestTable.objects.get(medicine=medid,shop=request.user)
            obj = MedicineTable.objects.get(pk=medid)
            ct = RequestTable.objects.get_or_create(medicine=obj,shop=request.user)
            if(ct[0].qty>0):
                return HttpResponse("<script>window.alert('already "+str(ct[0].qty)+" Quantity requested');window.location.href='/shop/all/stock/'</script>")
            else:
                ct[0].qty = qty
                ct[0].save()
            return redirect('shop_all_stock')
        else:
            return redirect('shop_all_stock')

def ManageStock(request):
    if request.method == 'GET':
        context = {}
        context['data'] = RequestTable.objects.filter(shop=request.user.id,status__gte=1)
        return render(request, 'shop/manage.html', context)
    elif request.method == 'POST':
        id = request.POST['reqid']
        p = request.POST['price']
        req = RequestTable.objects.get(pk=id)
        req.price = p
        req.status = 2
        req.save()
        return redirect('shop_manage_stock')

def RequestStock(request):
    if request.method == 'GET':
        context = {}
        context['data'] = RequestTable.objects.filter(shop=request.user.id,status=0)
        return render(request, 'shop/request.html', context)
    elif request.method == 'POST':
        id = request.POST['reqid']
        req = RequestTable.objects.get(pk=id)
        req.delete()
        return redirect('shop_request_stock')

def Delete(request,id):
    req = RequestTable.objects.get(pk=id)
    req.delete()
    return redirect('shop_manage_stock')

def ReRequest(request):
    if request.method == 'POST':
        id = request.POST['reqid']
        qty = request.POST['qty']
        req = RequestTable.objects.get(pk=id)
        req.qty = qty
        req.status = 0
        req.save()
        return redirect('shop_manage_stock')

def Order(request):
    if request.method == 'GET':
        context = {}
        context['data'] = OrderTable.objects.filter(product__shop=request.user.id,status=0)
        return render(request, 'shop/order.html', context)

def OrderAccept(request,id):
    if request.method == 'GET':
        obj = OrderTable.objects.get(pk=id)
        obj.status = 1
        obj.save()
        return redirect('shop_order')

def OrderHistory(request):
    if request.method == 'GET':
        context = {}
        context['data'] = OrderTable.objects.filter(product__shop=request.user.id,status=1)
        return render(request, 'shop/history.html', context)

