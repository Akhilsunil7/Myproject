from django.urls import path
from webapp import views

urlpatterns=[
    path('home_pg/',views.home_pg,name="home_pg"),
    path('about_us/',views.about_us,name="about_us"),
    path('contact_us/',views.contact_us,name="contact_us"),
    path('cat_pg/',views.cat_pg,name="cat_pg"),
    path('prod_pg/<cat_name>',views.prod_pg,name="prod_pg"),
    path('cart_pg/',views.cart_pg,name="cart_pg"),
    path('single_pro/<int:dataid>/',views.single_pro,name="single_pro"),
    path('registerpage/',views.registerpage,name="registerpage"),
    path('userpage/',views.userpage,name="userpage"),

    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('cartsave/',views.cartsave,name="cartsave"),
    path('deletecart/<int:cartid>/',views.deletecart,name="deletecart")
]
