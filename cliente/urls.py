
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.cliente_view, name='cliente_view'),
    path('<int:pk>', views.cliente_view, name='cliente_view'),
]