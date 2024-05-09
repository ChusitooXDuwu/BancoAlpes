from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse


#home deprecated
def home(request):
    return HttpResponse("Hello world! Django views")
def index(request):
    return render(request, 'index.html')

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

def health_check(request):
    return JsonResponse({'message': 'OK'}, status=200)

#def fucntion that callls  pdf from folder docClientes
