#cretae url to docuemtnos so i can lok fot them in the djangoa dmin

from django.contrib import admin
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path('', views.tarjetas_view, name='tarjetas_view'),
    path('<int:pk>', views.tarjeta_view, name='tarjetao_view'),
    path('tarjetacreate/', csrf_exempt(views.tarjeta_create), name='tarjetaCreate'),
    path('tarjetadeleteall/', csrf_exempt(views.tarjetas_deleteAll), name='tarjetaDeleteAll'),
    path('tarjetadelete/', csrf_exempt(views.tarjeta_delete), name='tarjetaDelete'),
    path('docCreate/', csrf_exempt(views.docCreate), name='docCreate'),
    path('tarjetas/', csrf_exempt(views.crear_tarjeta), name='crear_tarjeta')
]