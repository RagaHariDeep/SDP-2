from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
import datetime
from . models import DineInTables,Rooms
from . forms import addroomform,addtableform
from django.views.generic import TemplateView
# Create your views here.

def adminhomepage(request):
    bookedcount=[]
    tbookedcount=[]
    bookedcount.append(Rooms.objects.filter(is_available=False).count())
    bookedcount.append(Rooms.objects.filter(is_available=True).count())
    tbookedcount.append(DineInTables.objects.filter(is_available=False).count())
    tbookedcount.append(DineInTables.objects.filter(is_available=True).count())
    return render(request,"adminhome.html",{"bookedcount":bookedcount,"tbookedcount":tbookedcount})

def adminaddroom(request):
    if request.session.get("adminlogin",None):
        if request.method=="POST":
            form=addroomform(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect("adminviewrooms")
        else:
            form=addroomform()
        return render(request,"adminaddroom.html",{"form":form})
    else:
        return redirect("loginpage")

def adminupdateroom(request,roomno):
    if request.session.get("adminlogin",None):
        obj=Rooms.objects.get(room_no=roomno)
        form=addroomform(instance=obj)
        if request.method=="POST":
            form=addroomform(request.POST,request.FILES,instance=obj)
            if form.is_valid():
                form.save()
                return redirect("adminviewrooms")
        return render(request,"adminaddroom.html",{"form":form})
    else:
        return redirect("loginpage")

def adminviewrooms(request):
    if request.session.get("adminlogin",None):
        data=Rooms.objects.all()
        return render(request,"adminviewrooms.html",{"data":data})
    else:
        return redirect("loginpage")

def admindeleteroom(request,roomno):
    if request.session.get("adminlogin",None):
        Rooms.objects.filter(room_no=roomno).delete()
        return redirect("adminviewrooms")
    else:
        return redirect("loginpage")

def adminaddtable(request):
    if request.session.get("adminlogin",None):
        if request.method=="POST":
            form=addtableform(request.POST)
            if form.is_valid():
                form.save()
                return redirect("adminviewtables")
        else:
            form=addtableform()
        return render(request,"adminaddtable.html",{"form":form})
    else:
        return redirect("loginpage")

def adminviewtables(request):
    if request.session.get("adminlogin",None):
        data=DineInTables.objects.all()
        return render(request,"adminviewtables.html",{"data":data})
    else:
        return redirect("loginpage")

def adminupdatetable(request,tableno):
    if request.session.get("adminlogin",None):
        obj=DineInTables.objects.get(table_no=tableno)
        form=addtableform(instance=obj)
        if request.method=="POST":
            form=addtableform(request.POST,instance=obj)
            if form.is_valid():
                form.save()
                return redirect("adminviewtables")
        return render(request,"adminaddtable.html",{"form":form})
    else:
        return redirect("loginpage")

def admindeletetable(request,tableno):
    if request.session.get("adminlogin",None):
        DineInTables.objects.filter(table_no=tableno).delete()
        return redirect("adminviewtables")
    else:
        return redirect("loginpage")

def chartsdata(request):
    labels = []
    labels2=[]
    data = []
    data2=[]
    tbookedcount=[]
    data.append(Rooms.objects.filter(is_available=False).count())
    data2.append(Rooms.objects.filter(is_available=False).count())
    data2.append(DineInTables.objects.filter(is_available=False).count())
    data.append(Rooms.objects.filter(is_available=True).count())
    tbookedcount.append(DineInTables.objects.filter(is_available=False).count())
    tbookedcount.append(DineInTables.objects.filter(is_available=True).count())
    
    return JsonResponse(data={
        'labels': ["booked","available"],
        'labels2':["Room Bookings","Table Bookings"],
        'data': data,
        'data2':tbookedcount,
        'data3':data2,
    })