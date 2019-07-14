"""Project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('choice/', views.redirect),
    path('logincheck/', views.loginCheck),
    path('submit/', views.registration),
    path('searchCustomer', views.searchCustomer),
    path('showCustomers/', views.showCustomers),
    path('searchEmployee', views.searchEmployee),
    path('showEmployees/', views.showEmployees),
    path('initiateSessionView/', views.initiateSessionView),
    path('initiateLockerSession/', views.initiateLockerSession),
    path('remote/', views.remote),
    path('connect/', views.connect),
]
urlpatterns += staticfiles_urlpatterns()
