from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth import authenticate, login, logout
from shop.models import RequestTable, CartTable, ReviewTable, OrderTable
from dealer.models import MedicineTable
from .distance import get_distance
from .models import ShopTable


# Create your views here.

def Home(request):
    context = {}
    if str(request.user) != 'AnonymousUser':
        context['data2'] = CartTable.objects.filter(customer=request.user).count()
    if request.method == 'GET':
        context['data'] = RequestTable.objects.filter(status=2)
        return render(request, 'guest/home.html', context)
    elif request.method == 'POST':
        se = request.POST['search']
        position1 = [float(request.POST['lati']), float(request.POST['long'])]
        obj = RequestTable.objects.filter(status=2, medicine__name__contains=se)
        lst = []
        for i in obj:
            obj2 = ShopTable.objects.get(shop=i.shop.id)
            position2 = [float(obj2.latitude), float(obj2.longitude)]
            distance = get_distance(point1=position1, point2=position2)
            print(distance)
            if distance < 50:
                lst.append([i, int(distance)])
        context['data3'] = lst
        return render(request, 'guest/home.html', context)


def ProductView(request, id):
    if request.method == 'GET':
        context = {}
        # print(RequestTable.objects.get(pk=id).medicine.image)
        context['data'] = RequestTable.objects.get(pk=id)
        context['data1'] = ReviewTable.objects.filter(shop_med=id).order_by('-date')
        if str(request.user) != 'AnonymousUser':
            context['data2'] = CartTable.objects.filter(customer=request.user).count()
        return render(request, 'guest/product.html', context)
    elif request.method == 'POST':
        if str(request.user) != 'AnonymousUser':
            medid = request.POST['reqid']
            qty = request.POST['qty']
            obj = RequestTable.objects.get(pk=medid)
            if int(qty) < obj.qty:
                CartTable.objects.create(qty=qty, customer=request.user, product=obj)
                return HttpResponse(
                    "<script>window.alert('Item successfully added to the cart');window.location.href='/'</script>")
            else:
                return HttpResponse(
                    "<script>window.alert('Stock not available!');window.location.href='/view/product/%s'</script>" % medid)
        else:
            return redirect('guest_login')


def UpdateCart(request):
    id = request.POST['cartid']
    qty = request.POST['qty']
    pid = request.POST['pid']
    obj0 = RequestTable.objects.get(pk=pid)
    if int(qty) < obj0.qty:
        obj = CartTable.objects.get(pk=id)
        obj.qty = qty
        obj.save()
        return redirect('guest_cart_view')
    else:
        return HttpResponse(
            "<script>window.alert('Stock not available!');window.location.href='/customer/cart/'</script>")


def Login(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'guest/login.html', context)
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect("admin_home")
            else:
                if user.user_type == 'customer':
                    return redirect("guest_home")
                elif user.user_type == 'dealer':
                    return redirect("dealer_home")
                elif user.user_type == 'shop':
                    return redirect("shop_home")
        else:
            context = {}
            context['error'] = 'Invalid User or Admin not approved'
            context['uname'] = username
            return render(request, 'guest/login.html', context)


def Customer(request):
    if request.method == 'GET':
        context = {}
        context['form'] = CommonRegForm()
        return render(request, 'guest/create_customer.html', context)
    elif request.method == 'POST':
        form = CommonRegForm(request.POST)
        if form.is_valid():
            pawd = form.cleaned_data['password']
            obj = form.save(commit=False)
            obj.set_password(pawd)
            obj.user_type = 'customer'
            obj.save()
            return redirect('guest_customer')
        else:
            context = {}
            context['form'] = form
            return render(request, 'guest/login.html', context)


def Dealer(request):
    if request.method == 'GET':
        context = {}
        context['form'] = CommonRegForm()
        return render(request, 'guest/create_dealer.html', context)
    elif request.method == 'POST':
        form = CommonRegForm(request.POST)
        if form.is_valid():
            pawd = form.cleaned_data['password']
            obj = form.save(commit=False)
            obj.set_password(pawd)
            obj.is_active = 0
            obj.user_type = 'dealer'
            obj.save()
            return redirect('guest_home')
        else:
            context = {}
            context['form'] = form
            return render(request, 'guest/create_dealer.html', context)


def Shop(request):
    if request.method == 'GET':
        context = {}
        context['form1'] = CommonRegForm()
        context['form2'] = ShopRegForm()
        return render(request, 'guest/create_shop.html', context)
    elif request.method == 'POST':
        form1 = CommonRegForm(request.POST)
        form2 = ShopRegForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            pawd = form1.cleaned_data['password']
            obj = form1.save(commit=False)
            obj.set_password(pawd)
            obj.is_active = 0
            obj.user_type = 'shop'
            obj1 = form2.save(commit=False)
            obj1.shop = obj
            obj.save()
            obj1.save()
            return redirect('guest_home')
        else:
            context = {}
            context['form1'] = form1
            context['form2'] = form2
            return render(request, 'guest/create_shop.html', context)


def Cart(request):
    if request.method == 'GET':
        context = {}
        context['data'] = CartTable.objects.filter(customer=request.user)
        if str(request.user) != 'AnonymousUser':
            context['data2'] = CartTable.objects.filter(customer=request.user).count()
        return render(request, 'guest/cart.html', context)
    elif request.method == 'POST':
        if str(request.user) != 'AnonymousUser':
            obj = CartTable.objects.filter(customer=request.user)
            total = request.POST['total']
            for i in obj:
                obj1 = RequestTable.objects.get(pk=i.product.id)
                t = float(i.qty) * float(i.product.price)
                OrderTable.objects.create(qty=i.qty, total=t, product=i.product, customer=request.user)
                obj0 = CartTable.objects.get(pk=i.id)
                obj0.delete()
                new_qty = int(obj1.qty) - int(i.qty)
                obj1.qty = new_qty
                obj1.save()
            return HttpResponse("<script>window.alert('Item successfully ordered');window.location.href='/'</script>")


def RemoveProduct(request, id):
    obj = CartTable.objects.get(pk=id)
    obj.delete()
    return redirect('guest_cart_view')


def Logout(request):
    logout(request)
    return redirect('guest_login')


def PostReview(request):
    if request.method == 'POST':
        if str(request.user) != 'AnonymousUser':
            ti = request.POST['title']
            des = request.POST['review']
            r = request.POST['rating']
            med = request.POST['medid']
            obj_rv = ReviewTable.objects.filter(customer=request.user.id, shop_med=med)
            obj_od = OrderTable.objects.filter(customer=request.user.id, product=med)
            if obj_od.count() != 0:
                if obj_rv.count() == 0:
                    obj = RequestTable.objects.get(pk=med)
                    ReviewTable.objects.create(title=ti, description=des, rating=r, customer=request.user, shop_med=obj)
                else:
                    return HttpResponse(
                        "<script>window.alert('Already Reviewed this product !');window.location.href='/view/product/%s'</script>" % str(
                            med))
            else:
                return HttpResponse(
                    "<script>window.alert('You must purchase product then review it !');window.location.href='/view/product/%s'</script>" % str(
                        med))

            return redirect('/view/product/' + str(med))
        else:
            return redirect('guest_login')


def Orders(request):
    if request.method == 'GET':
        context = {}
        context['data'] = OrderTable.objects.filter(customer=request.user.id)
        return render(request, 'guest/orders.html', context)
