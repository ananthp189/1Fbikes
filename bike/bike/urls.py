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
    path('login2/', views.login),  # 用于打开登录页面
    #path('register/', views.register),  # 用于打开注册页面
   # path('register/save', views.save),  # 输入用户名密码后交给后台save函数处理
    path('login2/query', views.query),  # 输入用户名密码后交给后台query函数处理
    path('mianpage/', views.main),
]
urlpatterns += staticfiles_urlpatterns()