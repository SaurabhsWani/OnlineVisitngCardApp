from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()

#about us view
def about(request):
    return render(request, 'aboutus.html')
def contact(request):
    return render(request, 'contactus.html')
# View profile view    
def editProfile(request):
    if request.user.is_authenticated and request.method=='POST':
        pagenavigation='profile'
        name=request.POST.get('name')
        email=request.POST.get('email')
        phoneNumber=request.POST.get('phoneNumber')
        address=request.POST.get('address')
        if User.objects.filter(id=request.user.id).exists():
            User.objects.update(first_name=name,address=address,mobile=phoneNumber)#email=email,
            messages.info(request,"Profile Updated Successfully!")
        else:
            messages.info(request,"User Does Not Exist!")
        return render(request,'profile.html',{'pagenavigation':pagenavigation})
    else:
        return redirect('login')
# View profile view    
def profile(request):
    if request.user.is_authenticated:
        pagenavigation='profile'
        return render(request,'profile.html',{'pagenavigation':pagenavigation})
    else:
        return redirect('login')
# user order history view     
def UserOrderHistory(request):
    if request.user.is_authenticated:
        pagenavigation='orderhistory'
        userOrderHistory=OrderHistory.objects.select_related('ucid').filter(ucid__uid=request.user.id)
        return render(request,'orderHistory.html',{'userOrderHistory':userOrderHistory,'pagenavigation':pagenavigation})
    else:
        pagenavigation='home'
        return redirect('/',{'pagenavigation':pagenavigation})
#save edited card view
def SaveEditedCard(request):
    if request.user.is_authenticated:
        pagenavigation='home'
        heading=request.POST.get('heading')
        subheading=request.POST.get('subheading')
        address=request.POST.get('address')
        website=request.POST.get('website')
        phone=request.POST.get('phone')
        card=request.POST.get('card')
        cid=Card.objects.filter(cid=card)
        cid=cid[0] 
        uid=request.user.id
        UserEditedCardInformation=UserCardInformation.objects.create(heading=heading,subheading=subheading,address=address,website=website,mobile=phone,cid=cid,uid=uid)
        UserEditedCardInformation.save() 
        UserOrderHistory=OrderHistory.objects.create(ucid=UserEditedCardInformation,ordstatus='Pending')
        UserOrderHistory.save()
        messages.info(request,"Card Ordered Successfully Created Succesfully!")
        return redirect('/',{'pagenavigation':pagenavigation})
    else:
        return redirect('login')
# edit given card view
def EditCard(request):
    if request.user.is_authenticated and request.POST.get('card') != None:
        pagenavigation='home'
        card=request.POST.get('card')
        style=request.POST.get('style')
        return render(request,'singleCard.html',{'card':card,'style':style,'pagenavigation':pagenavigation})
    else:
        return redirect('login')
# Home Page VIew
def HomePageView(request):
    if request.user.is_authenticated:
        pagenavigation='home'
        cards = Card.objects.all()
        return render(request,'index.html',{'cards':cards,'pagenavigation':pagenavigation})
    else:
        return redirect('login')
# Logout view 
def logout(request):
    auth.logout(request)
    return redirect('/login')
# User login view
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user = auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            pagenavigation='home'
            return redirect('/',{'pagenavigation':pagenavigation})
        else:
            messages.info(request,"Invalid Credential")
            return redirect('/login')
    else:
        return render(request, 'login.html')        
# Regiset user view
def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        address=request.POST['address']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email taken")
                return redirect('/register')        
            elif User.objects.filter(mobile=mobile).exists():
                messages.info(request,"Mobile taken")
                return redirect('/register')        
            else:
                user=User.objects.create_user(password=password,email=email,first_name=name,address=address,mobile=mobile)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password not matching...")
            return redirect('register')        
    else:
        return render(request,'register.html')