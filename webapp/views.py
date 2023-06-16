from django.shortcuts import render,redirect
from superapp.models import categorydb,productdb
from webapp.models import userdb
from webapp.models import cartdb
from django.contrib import messages

# Create your views here.
def home_pg(req):
    data=categorydb.objects.all()
    return render(req,"Home.html",{'data':data})
def about_us(req):
    return render(req,"About.html")
def contact_us(req):
    return render(req,"Contact.html")
def cat_pg(req):
    data=categorydb.objects.all()
    return render(req,"Category.html",{'data':data})
def prod_pg(req,cat_name):
    prod=productdb.objects.filter(Category=cat_name)
    return render(req,"product.html",{'prod':prod})
def cart_pg(req):
    data=cartdb.objects.all()
    return render(req,"cart.html",{"data":data})
def cartsave(request):
    if request.method=="POST":
        unm=request.POST.get("uname")
        pn=request.POST.get("proname")
        pr=request.POST.get("price")
        qt=request.POST.get("qty")
        tl=request.POST.get("ttl")
        obj=cartdb(Username=unm,ProductName=pn, Quantity=qt,Price=pr,ProductImage=tl)
        obj.save()
        messages.success(request,"Saved Successfully")
        return redirect(cart_pg)
def single_pro(req,dataid):
    prosingle=productdb.objects.get(id=dataid)
    return render(req,"singleproduct.html",{'prosingle':prosingle})
def registerpage(req):
    return render(req,"Register.html")
def userpage(req):
    if req.method=="POST":
        un=req.POST.get('uname')
        em=req.POST.get('email')
        mb=req.POST.get('mob')
        ps=req.POST.get('pass')
        im=req.FILES.get['img']
        obj2=userdb(username=un,email=em,mobile=mb,password=ps,image=im)
        obj2.save()
        return redirect(registerpage)

def user_login(req):
    if req.method=="POST":
        em=req.POST.get('email')
        ps=req.POST.get('pass')
        if userdb.objects.filter(email=em,password=ps).exists():
            req.session['email']=em
            req.session['pass']=ps
            return redirect(home_pg)
        else:
            return redirect(registerpage)
    else:
        return redirect(registerpage)
def user_logout(req):
    del req.session['email']
    del req.session['pass']
    return redirect(registerpage)

def deletecart(request,cartid):
    cart=cartdb.objects.filter(id=cartid)
    cart.delete()
    messages.success(request,"Deleted Successfuly")
    return redirect(cart_pg)
