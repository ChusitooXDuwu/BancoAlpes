from ..models import tarjeta

def get_tarjeta(tarjeta_pk):
    tarjeta = tarjeta.objects.get(pk=tarjeta_pk)
    return tarjeta

def get_tarjetas():
    tarjetas = tarjeta.objects.all()
    return tarjetas

def create_tarjeta(form):
    tarjeta = form.save()
    'now close the tarjeta'

    tarjeta.save()

    return ("wiiiii creadoooooo")

def delete_all_tarjetas():
    tarjeta.objects.all().delete()
    return ("wiiiii eliminadoooos")


def delete_tarjeta(tarjeta_pk):
    tarjeta = tarjeta.objects.get(pk=tarjeta_pk)
    tarjeta.delete()
    return ("wiiiii eliminadoooos")

def create_doc(data):
    print(data)
    tarjeta = tarjeta(
        cliente=data['cliente'],
        tipo=data['tipo'],
        estado=data['estado'],
        score_confiabilidad=data['score_confiabilidad'],
        archivo=data['archivo']
    )
    tarjeta.save()
    return tarjeta