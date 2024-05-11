
from django.utils.deprecation import MiddlewareMixin

class RemoveCOOPHeaderMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response.headers.pop('Cross-Origin-Opener-Policy', None)
        return response
