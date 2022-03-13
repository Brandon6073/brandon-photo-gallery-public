"""photogallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.conf import settings # for media path
from django.conf.urls.static import static #static function to configure the media path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photogalleryapp.urls')),#include urls.py from inside the app


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
# use media_url and go to media root and find the image
# to view the image in admin pannel
# same with css