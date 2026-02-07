from django.urls import path
from .import views

urlpatterns = [
    path("",views.home,name="shop-home"),
    path("produts/",views.products,name="shop-produts"),

]