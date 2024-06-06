from django.urls import path
from Backend import views

urlpatterns = [
    path('indexpage/', views.indexpage, name="indexpage"),

    path('categorypage/', views.categorypage, name="categorypage"),
    path('categorydisplay/', views.categorydisplay, name="categorydisplay"),
    path('categorysave/', views.categorysave, name="categorysave"),
    path('categoryedit/<int:categoryid>/', views.categoryedit, name="categoryedit"),
    path('categoryupdate/<int:categoryid>/', views.categoryupdate, name="categoryupdate"),
    path('categorydelete/<int:categoryid>/', views.categorydelete, name="categorydelete"),

    path('productspage/', views.productspage, name="productspage"),
    path('productdisplay/', views.productdisplay, name="productdisplay"),
    path('productsave/', views.productsave, name="productsave"),
    path('productedit/<int:productid>/', views.productedit, name="productedit"),
    path('productupdate/<int:productid>/', views.productupdate, name="productupdate"),
    path('productdelete/<int:productid>/', views.productdelete, name="productdelete"),

    path('loginpage/', views.loginpage, name="loginpage"),
    path('admin_page/', views.admin_page, name="admin_page"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),

    path('contactdetails/', views.contactdetails, name="contactdetails"),
    path('delete_contact/<int:delid>/', views.delete_contact, name="delete_contact"),

]
