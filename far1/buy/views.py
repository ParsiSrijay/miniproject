from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Buyer,Bid
from app1.models import Farmer,Crop
# Create your views here.
user=''
farmer=''
crop=''
cost=0
buyer=''
location=''
Quantity=0
def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        aadhar_no = request.POST['ano']
        buys=request.POST['drop']
        username = request.POST['user']
        pass1 = request.POST['pass']
        pass2 = request.POST['pass1']
        phone_no = request.POST['phno']
        State = request.POST['state']
        District = request.POST['district']
        location = request.POST['location']
        email=request.POST['email']
        cname=request.POST['cname']
        lno=request.POST['lno']
        companyreg=request.POST['creg']
        if pass1 != pass2:
            return render(request, "buy.html", {'content': 'Enter the password again correctly'})
        elif len(aadhar_no) != 12:
            return render(request, "buy.html", {'content': 'Enter Correct Aadhar Number'})
        elif len(phone_no) != 10:
            return render(request, "buy.html", {'content': 'Enter correct Phone Number'})
        else:
            b = Buyer(Name=name, Aadhar_Number=aadhar_no,Type=buys, Phone_Numbers=phone_no, UserName=username, Password=pass2,
                       State=State, District=District, Area=location,Email=email,Company_name=cname,LNO=lno,Company_Reg=companyreg)
            b.save()
            u = User(username=username, password=pass2)
            u.save()
            return render(request,"re.html",{'content':username})
    else:
        return render(request,'buy.html')
def signin(request):
    if request.method=="POST":
        global user,u
        user=request.POST['username']
        passw=request.POST['pass']
        u=User.objects.get(username=user,password=passw)
        if u is None:
            return render(request,'aa.html',{'content':'Enter correct username or Password'})
        else:
            return render(request,'re.html',{'content':user})
    else:
        return render(request,"aa.html")
def placeorder(request):
    if request.method =="POST":
        global buyer,location,Quantity,crop
        buyer=request.POST.get('buy',False)
        location=request.POST.get('loc',False)
        Quantity=request.POST.get('quantity',False)
        crop=request.POST.get('crop',False)
        f =Farmer.objects.raw('SELECT * FROM app1_crop,app1_farmer where app1_crop.Username=app1_farmer.Username and CropName=%s and Area=%s',[crop,location])
        return render(request,"orders.html",{"content":f})
    return render(request,"placeorder.html")

def confirm(request):
    if request.method=="POST":
        far=request.POST['far']
        f = Farmer.objects.raw(
            'SELECT * FROM app1_crop,app1_farmer where app1_crop.Username=app1_farmer.Username and CropName=%s and Area=%s and app1_farmer.Username=%s',
            [crop, location,far])
        amt = 0
        name = ''
        b = Buyer.objects.get(UserName=user)
        bphone = b.Phone_Numbers
        for x in f:
            amt = x.MinCost
            phno = x.Phone_Numbers
        b = Bid(Buyer=buyer, Farmer=far, Quantity=Quantity, Crop=crop, Price=amt, BPhone=bphone, FPhone=phno)
        b.save()
        c = Crop.objects.get(Username=far, CropName=crop)
        c.MinCost = c.MinCost + 10
        c.save()
        return render(request, 'CompleteBid.html')
    else:
        return render(request,"abc.html")



def orderlist(request):
    b=Bid.objects.raw('SELECT * FROM buy_bid WHERE Buyer=%s',[user])
    return render(request,'orderlist.html',{'content':b})

