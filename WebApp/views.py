from django.shortcuts import render, redirect
from Backend.models import CategoryDB, ProductDB
from WebApp.models import ContactDB, RegisterDB, WishlistDB, OrderDB
from django.contrib import messages
import razorpay
from django.http import JsonResponse


# Create your views here.
def homepage(request):
    cat = CategoryDB.objects.all()
    return render(request, "Home.html", {'cat': cat})


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
    data = ProductDB.objects.filter(Category=cat_name)
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
        un = request.POST.get("username")
        pi = request.POST.get('productid')
        cn = request.POST.get("carname")
        pr = request.POST.get("price")
        obj = WishlistDB(Username=un, ProductID=pi, Carname=cn, Price=pr)
        obj.save()
        messages.success(request, "Successfully added to wishlist. ❤️😍")
        return redirect(homepage)


def wishlistpage(request, proid=None):
    username = request.session.get('Username')
    if not username:
        return redirect('login')

    data = WishlistDB.objects.filter(Username=username)
    subtotal = sum(int(item.Price) for item in data)
    insurance = 380000
    total = subtotal + insurance

    return render(request, "wishlist.html", {
        'data': data,
        'username': username,
        'subtotal': subtotal,
        'total': total,
        'insurance': insurance
    })


def delete_item(request, p_id):
    x = WishlistDB.objects.filter(id=p_id)
    x.delete()
    messages.warning(request, "Product removed from wishlist")
    return redirect(wishlistpage)


def checkoutpage(request):
    username = request.session.get('Username')
    data = WishlistDB.objects.filter(Username=username)
    subtotal = sum(int(item.Price) for item in data)
    insurance = 380000
    total = subtotal + insurance

    if request.method == 'POST':
        un = request.POST.get('name')
        em = request.POST.get('email')
        ph = request.POST.get('phone')
        add = request.POST.get('address')
        desc = request.POST.get('description')
        obj = OrderDB(Username=un, Email=em, Phone=ph, Address=add, Description=desc, Price=total)
        obj.save()
        return redirect(paymentpage)

    return render(request, "checkout.html", {'Product': data, 'total': total})


def paymentpage(request):
    customer = OrderDB.objects.order_by('-id').first()

    if customer is None:
        return redirect('wishlistpage')

    payy = customer.Price

    try:
        payy = int(payy)
    except ValueError:
        return redirect('wishlistpage')

    amount = payy * 100
    payy_str = str(amount)

    if request.method == 'POST':
        order_currency = "INR"
        client = razorpay.Client(auth=('rzp_test_Xe8qXi9C0xosm3', 'XcZsUeKUQZUqD7FF8xKcZT2H'))
        payment = client.order.create({'amount': amount, 'currency': order_currency, 'payment_capture': '1'})

        return render(request, "payment.html", {'customer': customer, 'payy_str': payy_str, 'payment': payment})

    return render(request, "payment.html", {'customer': customer, 'payy_str': payy_str})


def saveorder(request):
    if request.method == 'POST':
        un = request.POST.get('name')
        em = request.POST.get('email')
        ph = request.POST.get('phone')
        add = request.POST.get('address')
        desc = request.POST.get('description')
        pr = request.POST.get('price')
        obj = OrderDB(Username=un, Email=em, Phone=ph, Address=add, Description=desc, Price=pr)
        obj.save()
        return redirect(paymentpage)
