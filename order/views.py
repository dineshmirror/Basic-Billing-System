from django.shortcuts import render,redirect
from .models import *
from django.views import View
from django.contrib import messages


def ItemModelView(request):
    form = ItemModel()
    if request.method=='POST':
        item_name = request.POST.get('item_name')
        quantity=int(request.POST.get("quantity"))
        quantity_unit = request.POST.get('quantity_unit')
        price=int(request.POST.get("price"))
        total_price=quantity*price
        date = request.POST.get('date')

        get = ItemModel.objects.create(
                                item_name = item_name,
                                quantity = quantity,
                                quantity_unit = quantity_unit,
                                price = price,
                                total_price = total_price
                                )

        get.save()
    return render(request,"order_details.html",{"form" : form})

def ItemView(request):
    getall = ItemModel.objects.all()
    custgetall=CustomerModel.objects.all()
    return render(request,"item_view.html",{"getall":getall,"custgetall":custgetall})



def CustomerModelView(request):
    customer = CustomerModel()
    if request.method=="POST":
        customer = CustomerModel(request.POST,request.FILES)
        customer_name = request.POST.get('customer_name')
        customer_mobile_number = request.POST.get('customer_mobile_number')
        cust_get = CustomerModel.objects.create(
                                customer_name = customer_name,
                                customer_mobile_number = customer_mobile_number
                                )
        cust_get.save()
    return render(request,"customer_details.html",{"customer":customer})




# Create your views here.
