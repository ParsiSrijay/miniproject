from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
from .forms import CropForm
from .models import Farmer,Crop,Bill
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from buy.models import Bid
user=''
def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        aadhar_no = request.POST['ano']
        username=request.POST['user']
        pass1=request.POST['pass']
        pass2=request.POST['pass1']
        phone_no = request.POST['phno']
        State = request.POST['state']
        District = request.POST['district']
        location = request.POST['location']
        if pass1!=pass2:
            return render(request,"test2.html",{'content':'Enter the password again correctly'})
        elif len(aadhar_no)!=12:
            return render(request,"test2.html",{'content':'Enter Correct Aadhar Number'})
        elif len(phone_no)!=10:
            return render(request,"test2.html",{'content':'Enter correct Phone Number'})
        else:
            f=Farmer(Name=name,Aadhar_Number=aadhar_no,Phone_Numbers=phone_no,UserName=username,Password=pass2,State=State,District=District
                     ,Area=location)
            f.save()
            u=User(username=username,password=pass2)
            u.save()
            return render(request,"test2.html",{'content':'Successfully Registered'})
    else:
        return render(request,"test2.html")
def signin(request):
    if request.method=="POST":
        global user
        user=request.POST['username']
        passw=request.POST['pass']
        u=User.objects.get(username=user,password=passw)
        if u is None:
            return render(request,'test1.html',{'content':'Enter correct username or Password'})
        else:
            crop = Crop.objects.filter(Username=user)
            return render(request,'a.html',{'content':user,'crop_images':crop})
    else:
        return render(request,"test1.html")


def CropDetails(request):
    if request.method == 'POST':
        form = CropForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CropForm()
    return render(request, 'w.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')

def displayOrder(request):
    b=Bid.objects.raw('SELECT * FROM buy_bid WHERE Farmer=%s',[user])
    return render(request,'far.html',{'content':b})

def confirm(request):
    if request.method=="POST":
        buy=request.POST['buy']
        b= Bid.objects.raw('SELECT * FROM buy_bid WHERE Buyer=%s',[buy])
        for x in b:
            phno1=x.BPhone
            phno2=x.FPhone
            amt=x.Price
            qunt=x.Quantity
            crop=x.Crop
        price=amt*qunt
        bill = Bill(FarmerName=user,BuyerName=buy,BPhone=phno1,FPhone=phno2,Cost=price,Crop=crop)
        bill.save()
        c=Crop.objects.get(Username=user,CropName=crop)
        q=c.Quantity
        c.Quantity=q-qunt
        c.save()
        return render(request,"sucess.html")
    else:
        return render(request,"def.html")



