# middlewares.py

from django.conf import settings

# middlewares.py
# middleware.py
# middleware.py
class XForwardedPortMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Ajustar el host y el puerto basado en 'X-Forwarded-Host' y 'X-Forwarded-Port'
        forwarded_host = request.META.get('HTTP_X_FORWARDED_HOST')
        forwarded_port = request.META.get('HTTP_X_FORWARDED_PORT')
        if forwarded_host:
            if forwarded_port:
                request.META['HTTP_HOST'] = f'{forwarded_host}:{forwarded_port}'
            else:
                request.META['HTTP_HOST'] = forwarded_host
        return self.get_response(request)


