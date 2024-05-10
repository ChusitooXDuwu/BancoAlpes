# middlewares.py

from django.conf import settings

# middlewares.py
class CompleteURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Establecer el esquema de la solicitud basado en 'X-Forwarded-Proto'
        forwarded_proto = request.META.get('HTTP_X_FORWARDED_PROTO')
        if forwarded_proto:
            request.scheme = forwarded_proto
        
        # Establecer el host y el puerto basado en 'X-Forwarded-Host' y 'X-Forwarded-Port'
        forwarded_host = request.META.get('HTTP_X_FORWARDED_HOST')
        forwarded_port = request.META.get('HTTP_X_FORWARDED_PORT')
        if forwarded_host:
            if forwarded_port:
                request.META['HTTP_HOST'] = f'{forwarded_host}:{forwarded_port}'
            else:
                request.META['HTTP_HOST'] = forwarded_host

        return self.get_response(request)
