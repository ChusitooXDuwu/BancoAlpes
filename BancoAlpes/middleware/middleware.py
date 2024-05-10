# middlewares.py

from django.conf import settings

# middlewares.py
class XForwardedPortMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Modificar el protocolo a 'http' usando la cabecera 'X-Forwarded-Proto'
        request.META['HTTP_X_FORWARDED_PROTO'] = 'http'
        
        # Ajustar el puerto si viene en la cabecera 'X-Forwarded-Port'
        forwarded_port = request.META.get('HTTP_X_FORWARDED_PORT')
        if forwarded_port:
            host = request.get_host().split(':')[0]
            request.META['HTTP_HOST'] = f'{host}:{forwarded_port}'
        response = self.get_response(request)
        return response

