"""BancoAlpes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
#from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

# from the folder tarjetas, import the views file
from tarjeta.views import pdf_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('home/', views.index),
    # path('cliente/', include('cliente.urls')),
    path('tarjetas/', include('tarjetas.urls')),
    path('health/', views.health_check, name='health'),
    path(r'', include('django.contrib.auth.urls')),
    path(r'', include('social_django.urls')),

    #path('tarjeta/', pdf_view, name='pdf_view'),    
]

if settings.DEBUG:
    urlpatterns += [
        
        path('health-check/', views.healthCheck),
    ]