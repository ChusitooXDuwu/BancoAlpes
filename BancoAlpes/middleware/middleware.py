# middlewares.py

from django.conf import settings

# middlewares.py
class XForwardedPortMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Establece el esquema de la solicitud a HTTP
        request.scheme = 'http'
        forwarded_port = request.META.get('HTTP_X_FORWARDED_PORT')
        if forwarded_port:
            host = request.get_host().split(':')[0]
            request.META['HTTP_HOST'] = f'{host}:{forwarded_port}'
        return self.get_response(request)
