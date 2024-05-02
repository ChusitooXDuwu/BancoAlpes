from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello world! Django views")

def healthCheck(request):
    return HttpResponse("ok")

# Render all kind of files
def pdf_view(request, *args, **kwargs):
    try:
        path = kwargs.get('path', '')
        with open(f'docClientes/{path}', 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=some_file.pdf'
            return response
    except FileNotFoundError:
        return HttpResponse("The file was not found")



#def fucntion that callls  pdf from folder docClientes
