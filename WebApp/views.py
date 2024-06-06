from django.shortcuts import render, redirect
from Backend.models import CategoryDB, ProductDB
from WebApp.models import ContactDB, RegisterDB, WishlistDB
from django.contrib import messages


# Create your views here.
def homepage(request):
    return render(request, "Home.html")


def aboutpage(request):
    return render(request, "About.html")


def contactpage(request):
    return render(request, "Contact.html")


def contactsave(request):
    if request.method == 'POST':
        na = request.POST.get('name')
        em = request.POST.get('email')
        msg = request.POST.get('message')
        obj = ContactDB(Name=na, Email=em, Message=msg)
        obj.save()
        return redirect(contactpage)


def aboutpage(request):
    return render(request, "About.html")


def carspage(request):
    cardata = ProductDB.objects.all()
    return render(request, "Cars.html", {'cardata': cardata})


def Single_Product(request, proid):
    data = ProductDB.objects.get(id=proid)
    return render(request, "SingleProduct.html", {'data': data})


def classes(request):
    return render(request, "Classes.html")


def filtered_products(request, cat_name):
    data = ProductDB.objects.filter(CategoryDB=cat_name)
    return render(request, "FilteredProducts.html", {'data': data})


# registration pages

def signinpage(request):
    return render(request, "login.html")


def registration_page(req):
    return render(req, "Signup.html")


def save_user(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        em = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        obj = RegisterDB(Username=un, Email=em, Password=pass1)
        if RegisterDB.objects.filter(Username=un).exists():
            messages.warning(request, "Username already exists..!")
        else:
            obj.save()
            messages.success(request, "Congrats, your registration succcessful")
        return redirect(registration_page)


def Userlogin(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        pswd = request.POST.get('password')
        if RegisterDB.objects.filter(Username=un, Password=pswd).exists():
            request.session['Username'] = un
            request.session['Password'] = pswd
            messages.success(request, "Login Successful")
            return redirect(homepage)
        else:
            messages.error(request, "Check your credentials..!")
            return redirect(registration_page)
    else:
        messages.error(request, "Check credentials..!")
        return redirect(registration_page)


def Userlogout(request):
    del request.session['Username']
    del request.session['Password']
    messages.warning(request, "Logged out")
    return redirect(registration_page)


def addWishlist(request):
    if request.method == 'POST':
        pi = request.POST.get("productid")
        cn = request.POST.get("carname")
        pr = request.POST.get("price")
        obj = WishlistDB(ProductID=pi, Carname=cn, Price=pr)
        obj.save()
        messages.success(request, "Successfully added to wishlist. ❤️😍")


def wishlistpage(request):
    return render(request, "wishlist.html")
