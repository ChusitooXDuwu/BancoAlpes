import os

from .forms import TarjetaForm
from .logic import logic_tarjetas as vl
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.urls import reverse
from .logic.logic_tarjetas import create_tarjeta
from .logic.logic_tarjetas import delete_all_tarjetas
from .logic.logic_tarjetas import delete_tarjeta
from django.contrib import messages
from BancoAlpes.auth0backend import getRole

@csrf_exempt
def tarjetas_view(request):
    role = getRole(request)
    if role == "Administrador":
        if request.method == 'GET':
            id = request.GET.get("id", None)
            if id:
                tarjetas_dto = vl.get_tarjeta(id)
                tarjetas = serializers.serialize('json', [tarjetas_dto,])
                return HttpResponse(tarjetas, 'application/json')
            else:
                tarjetas_dto = vl.get_tarjetas()
                tarjetas = serializers.serialize('json', tarjetas_dto)
                return HttpResponse(tarjetas, 'application/json')

        if request.method == 'POST':
            tarjetas_dto = vl.create_tarjetas(json.loads(request.body))
            tarjetas = serializers.serialize('json', [tarjetas_dto,])
            return HttpResponse(tarjetas, 'application/json')
    else:
        return HttpResponse("Unauthorized User")

@csrf_exempt
def tarjeta_view(request, pk):
    if request.method == 'GET':
        tarjetas_dto = vl.get_tarjeta(pk)
        tarjetas = serializers.serialize('json', [tarjetas_dto,])
        return HttpResponse(tarjetas, 'application/json')

    if request.method == 'PUT':
        tarjetas_dto = vl.update_tarjeta(pk, json.loads(request.body))
        tarjetas = serializers.serialize('json', [tarjetas_dto,])
        return HttpResponse(tarjetas, 'application/json')

   
@csrf_exempt
def tarjeta_create(request):
    if request.method == 'POST':
        
        form = TarjetaForm(request.POST)
        create_tarjeta(form)
        messages.add_message(request, messages.SUCCESS, 'tarjeta create successful')
        print("tarjeta create successful")
        return HttpResponseRedirect(reverse('tarjetaCreate')) 
        # if form.is_valid():
        #     create_tarjeta(form)
        #     messages.add_message(request, messages.SUCCESS, 'tarjeta create successful')
        #     print("tarjeta create successful")
        #     return HttpResponseRedirect(reverse('tarjetaCreate')) 
        # else:
        #     print(form.errors)
    else:
        form = TarjetaForm()

    context = {
        'form': form,
    }

    return HttpResponse("el form no es correcto, revisar entradas o infromacion enviada")

@csrf_exempt
def tarjetas_deleteAll(request):
    role = getRole(request)
    if role == "Administrador":
        if request.method == 'GET':
            print('deleting all tarjetas')
            delete_all_tarjetas()
            return HttpResponse("All tarjetas deleted", 'application/json')
        #else:
            #return HttpResponse("Method not allowed", 'application/json')
    else:
        return HttpResponse("Unauthorized User")    
    
    
@csrf_exempt
def tarjeta_delete(request, pk):
    role = getRole(request)
    if role == "Administrador":
        if request.method == 'GET':
            print('deleting tarjeta')
            delete_tarjeta(pk)
            return HttpResponse("tarjeta deleted", 'application/json')
        else:
            return HttpResponse("Method not allowed", 'application/json')
    else:
        return HttpResponse("Unauthorized User")
 
    
@csrf_exempt
def docCreate(request):
    if request.method == 'POST':
        print("creating tarjeta")
        data = json.loads(request.body)
        print(data)
        doc_dto = vl.create_doc(json.loads(request.body))
        doc = serializers.serialize('json', [doc_dto,])
        return HttpResponse(doc, 'application/json')
    else:
        return HttpResponse("Method not allowed", 'application/json')