# middlewares.py

from django.conf import settings

class UseForwardedPortMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Extrae el puerto de la cabecera X-Forwarded-Port
        forwarded_port = request.META.get('HTTP_X_FORWARDED_PORT')
        if forwarded_port:
            # Añade el puerto al host actual en la request
            request.META['HTTP_HOST'] = f"{request.get_host().split(':')[0]}:{forwarded_port}"
        response = self.get_response(request)
        return response
