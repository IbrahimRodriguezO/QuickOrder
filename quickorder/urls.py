"""quickorder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path,include
from applications.users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LoginUser.as_view(), name="inicio-sesion"),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.owner.urls')),
    re_path('', include('applications.waiter.urls')),
    re_path('', include('applications.chef.urls')),
]
