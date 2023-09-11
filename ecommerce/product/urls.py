
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('soap', views.soap_page,name="soap"),
    path('surf',views.surf,name='surf'),
    path('cart',views.cart,name='cart'),
    path('search',views.search,name='search'),
    
]