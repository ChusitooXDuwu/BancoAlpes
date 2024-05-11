
from django.utils.deprecation import MiddlewareMixin

class RemoveCOOPHeaderMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        print("Modifying response headers to remove COOP")  # Agrega esto para depuración
        response.headers.pop('Cross-Origin-Opener-Policy', None)
        return response

