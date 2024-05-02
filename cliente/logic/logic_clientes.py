from ..models import Cliente

def get_clientes():
    clientes = Cliente.objects.all()
    return clientes

def get_cliente(client_pk):
    cliente = Cliente.objects.get(pk=client_pk)
    return cliente

def update_cliente(client_pk, new_client):
    cliente = get_cliente(client_pk)
    cliente.name = new_client["name"]
    cliente.save()
    return cliente

def create_cliente(client):
    cliente = Cliente(name=client["name"])
    cliente.save()
    return cliente