"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from app import views
from order.views import ordernaw
from login.views import loginpage
from contactus.views import contactUs
from sign_page.views import signpage
from Email.views import emailsubmit
from foodorder.views import orderfood
from feedback.views import feedbacks
from numberlogin.views import number


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('about-us/', views.about),
    path('contact-us/', views.contact),
    path('order/', ordernaw, name='order'),
    path('signpage/',signpage, name='signpage'),
    path('addition/',views.addition),
    path('Try/', views.Try),
    path('contact/',contactUs),
    path('', loginpage, name="loginpage"),
    path('emaillogin/',emailsubmit, name='email'),
    path('foodorder/', orderfood),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('feedback/', feedbacks, name='feedback'),
    path('numberwithlogin/', number, name='numberlogin'),
    path('thankyoufb/', views.thankyoufb, name='thankyoufb'),
    path('thankyoucu/', views.thankyoucu, name='thankyoucu'),
    path('search/', views.search, name='search'),
    path('auth/', include('auth_app.urls')),
   #   path('login/username/', login_username, name='login_username'),
   # path('login/email/', login_email, name='login_email'),
    
   
]
