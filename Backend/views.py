from django.shortcuts import render, redirect
from Backend.models import CategoryDB, ProductDB
from WebApp.models import ContactDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
def indexpage(request):
    return render(request, "index.html")


# category section

def categorypage(request):
    return render(request, "category.html")


def categorydisplay(request):
    data = CategoryDB.objects.all()
    return render(request, "categorydisplay.html", {'data': data})


def categorysave(request):
    if request.method == 'POST':
        cn = request.POST.get('cname')
        desc = request.POST.get('description')
        cimg = request.FILES['cimage']
        obj = CategoryDB(CategoryName=cn, Description=desc, CategoryImage=cimg)
        obj.save()
        messages.success(request, "Category saved successfully..!")
        return redirect(categorypage)


def categoryedit(request, categoryid):
    data = CategoryDB.objects.get(id=categoryid)
    return render(request, "categoryedit.html", {'data': data})


def categorydelete(request, categoryid):
    x = CategoryDB.objects.filter(id=categoryid)
    x.delete()
    messages.error(request, "Deleted..!")
    return redirect(categorydisplay)


def categoryupdate(request, categoryid):
    if request.method == 'POST':
        cn = request.POST.get('cname')
        desc = request.POST.get('description')
    try:
        cimg = request.FILES['cimage']
        fs = FileSystemStorage()
        file = fs.save(cimg.name, cimg)
    except MultiValueDictKeyError:
        file = CategoryDB.objects.get(id=categoryid).CategoryImage
    CategoryDB.objects.filter(id=categoryid).update(CategoryName=cn, Description=desc, CategoryImage=file)
    messages.success(request, "Updated")
    return redirect(categorydisplay)


# product section

def productspage(request):
    cat = CategoryDB.objects.all()
    return render(request, "product.html", {'cat': cat})


def productdisplay(request):
    data = ProductDB.objects.all()
    return render(request, "productdisplay.html", {'data': data})


def productsave(request):
    if request.method == 'POST':
        ctn = request.POST.get('catname')
        prn = request.POST.get('proname')
        pr = request.POST.get('price')
        descr = request.POST.get('description')
        proimg = request.FILES['proimage']
        obj = ProductDB(Category=ctn, ProductName=prn, Price=pr, Description=descr, ProductImage=proimg)
        obj.save()
        return redirect(productspage)


def productupdate(request, productid):
    if request.method == 'POST':
        ctn = request.POST.get('catname')
        prn = request.POST.get('proname')
        pr = request.POST.get('price')
        descr = request.POST.get('description')
        try:
            proimg = request.FILES['proimage']
            fs = FileSystemStorage()
            file = fs.save(proimg.name, proimg)
        except MultiValueDictKeyError:
            file = ProductDB.objects.get(id=productid).ProductImage
            ProductDB.objects.filter(id=productid).update(Category=ctn, ProductName=prn, Price=pr, Description=descr,
                                                          ProductImage=file)
            return redirect(productdisplay)


def productedit(request, productid):
    pro = ProductDB.objects.get(id=productid)
    cat = CategoryDB.objects.all()
    return render(request, "productedit.html", {'pro': pro, 'cat': cat})


def productdelete(productid):
    x = ProductDB.objects.filter(id=productid)
    x.delete()
    return redirect(productdisplay)


# login, logout - for admin

def loginpage(request):
    return render(request, "adminlogin.html")


def admin_page(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=pwd)
            if x is not None:
                login(request, x)
                request.session['username'] = un
                request.session['password'] = pwd
                return redirect(indexpage)
            else:
                return redirect(loginpage)
    else:
        return redirect(loginpage)


def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)


def contactdetails(request):
    data = ContactDB.objects.all()
    return render(request, "ContactData.html", {'data': data})


def delete_contact(x, delid):
    x = ContactDB.objects.filter(id=delid)
    x.delete()
    return redirect(contactdetails)
