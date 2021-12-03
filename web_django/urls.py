"""web_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from django.shortcuts import render
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from hotel import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'trangchu/', views.trangchu, name='trangchu'),
    path(r'accounts/', include('login.urls')),
    path(r'weather/', include('weather.urls')),
    path(r'hotels/', include('hotel.urls')),
    path(r'camnang/', include('camnang.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
