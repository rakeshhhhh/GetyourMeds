from django.shortcuts import render, redirect
from .models import *
from .forms import *
from shop.models import RequestTable

# Create your views here.

def Home(request):
    context = {}
    return render(request,'dealer/home.html',context)


def CreateMedicine(request):
    if request.method == 'GET':
        context = {}
        context['form'] = MedForm()
        return render(request, 'dealer/medicine.html', context)
    elif request.method == 'POST':
        form = MedForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.dealer=request.user
            obj.save()
            return redirect('dealer_add_medicine')
        else:
            context = {}
            context['form'] = form
            return render(request, 'dealer/medicine.html', context)

def ManageMed(request):
    if request.method == 'GET':
        context = {}
        context['data'] = MedicineTable.objects.filter(dealer=request.user.id)
        return render(request, 'dealer/manage.html', context)

def DelMed(request,id):
    med = MedicineTable.objects.get(id=id)
    med.delete()
    return redirect('dealer_manage_medicine')

def UpMed(request,id):
    med = MedicineTable.objects.get(id=id)
    if request.method == 'GET':
        context = {}
        context['form'] = MedForm(instance=med)
        return render(request,'dealer/medicine.html',context)
    elif request.method == 'POST':
        form = MedForm(data=request.POST, instance=med)
        if form.is_valid():
            form.save()
            return redirect('dealer_manage_medicine')
        else:
            context = {}
            context['form'] = form
            return render(request,'dealer/medicine.html',context)

def RequestMed(request):
    if request.method == 'GET':
        context = {}
        # m = MedicineTable.objects.filter(dealer=request.user.id)
        # print(m)
        context['data'] = RequestTable.objects.filter(status=0,medicine__dealer=request.user.id) 
        return render(request, 'dealer/request.html', context)

def RequestAcpt(request,id):
    obj = RequestTable.objects.get(pk=id)
    obj.status=1
    obj.save()
    return redirect('dealer_request')