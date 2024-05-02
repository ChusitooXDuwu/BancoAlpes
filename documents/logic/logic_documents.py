from ..models import Documento

def get_document(document_pk):
    document = Documento.objects.get(pk=document_pk)
    return document

def get_documents():
    documents = Documento.objects.all()
    return documents

def create_document(form):
    document = form.save()
    'now close the document'

    document.save()

    return ("wiiiii creadoooooo")

def delete_all_documents():
    Documento.objects.all().delete()
    return ("wiiiii eliminadoooos")

def create_doc(data):
    print(data)
    document = Documento(
        cliente=data['cliente'],
        tipo=data['tipo'],
        estado=data['estado'],
        score_confiabilidad=data['score_confiabilidad'],
        archivo=data['archivo']
    )
    document.save()
    return document