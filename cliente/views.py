from .logic import logic_clientes as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def clientes_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            cliente_dto = vl.get_cliente(id)
            cliente = serializers.serialize('json', [cliente_dto,])
            return HttpResponse(cliente, 'application/json')
        else:
            clientes_dto = vl.get_clientes()
            clientes = serializers.serialize('json', clientes_dto)
            return HttpResponse(clientes, 'application/json')

    if request.method == 'POST':
        cliente_dto = vl.create_cliente(json.loads(request.body))
        cliente = serializers.serialize('json', [cliente_dto,])
        return HttpResponse(cliente, 'application/json')

@csrf_exempt
def cliente_view(request, pk):
    if request.method == 'GET':
        cliente = vl.get_cliente(pk)
        cliente_dto = serializers.serialize('json', cliente)
        return HttpResponse(cliente_dto, 'application/json')

    if request.method == 'PUT':
        cliente_dto = vl.update_cliente(pk, json.loads(request.body))
        cliente = serializers.serialize('json', [cliente_dto,])
        return HttpResponse(cliente, 'application/json')
    

@csrf_exempt
def cliente_detail(request, id):
    cliente = vl.get_cliente(id)
    data = {
        "id": cliente.id,
        "nombre": cliente.nombre,
        "apellido": cliente.apellido,
        "cedula": cliente.cedula,
        "email": cliente.email,
        "telefono": cliente.telefono,
        "direccion": cliente.direccion,
        "fecha_nacimiento": cliente.fecha_nacimiento,
        "fecha_creacion": cliente.fecha_creacion,
        "estado_documentos": cliente.estado_documentos
    }
    return JsonResponse(data)