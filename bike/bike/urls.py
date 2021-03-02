"""bike URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
from django.contrib import admin
from django.urls import include, path
from bikeapp import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.login),
    path('query/', views.query),
    path('login/', views.login),  # Used to open the login page
    path('register/', views.register),  # Used to open the register page
    path('register/save', views.save),  # After entering the user name and password, hand it to the background save function for processing
    path('login/query', views.query),  # After entering the user name and password, hand it to the background query function for processing
    path('mainpage/', views.main),
    path('manager/', views.query),
    path('operator/', views.query),
    path('defective/', views.defective),  #Open the Registration page
    path('defective/dd', views.dd),
    path('bikemap/', views.bikemap),
    path('movebike/', views.movebike),
    path('movebike/select', views.select),
    path('locationmap/',views.locationmap),
    path('return/', views.returnBike),   #Return bike using users id number
    path('rent/', views.rent),          # Rent a bike using users id number
    path('datavisualization/',views.dataVis),
    path('pay/',views.pay),
    path('movebike/', views.movebike),
    path('movebike/move', views.move),
    path('movebike/select', views.select),
    path('repairbike/', views.repairmap),
    path('repairbike/repair', views.repair),
    #path('locationbike/', views.locationbike),
    path('bar_rent_duration/', views.dv_rentbike),
    path("bheatmap/",views.dv_heatmapbike),
    path("pheatmap/",views.dv_heatmappay),
    path("busage/",views.dv_bikeusage),
    path("monthpay/", views.dv_monthpay),
    path("ustructure/", views.dv_ustructure),
    path("bstatus/", views.dv_bstatus),


    ]
urlpatterns += staticfiles_urlpatterns()
