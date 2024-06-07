from django.urls import path
from WebApp import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('carspage/', views.carspage, name="carspage"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('contactsave/', views.contactsave, name="contactsave"),
    path('carspage/', views.carspage, name="carspage"),
    path('classes/', views.classes, name="classes"),
    path('Single_Product/<int:proid>/', views.Single_Product, name="Single_Product"),
    path('filtered_products/', views.filtered_products, name="filtered_products"),
    path('signinpage/', views.signinpage, name="signinpage"),
    path('registration_page/', views.registration_page, name="registration_page"),
    path('save_user/', views.save_user, name="save_user"),
    path('Userlogin/', views.Userlogin, name="Userlogin"),
    path('Userlogout/', views.Userlogout, name="Userlogout"),
    path('wishlistpage/', views.wishlistpage, name="wishlistpage"),
    path('addWishlist/<int:proid>/', views.addWishlist, name="addWishlist"),

]
