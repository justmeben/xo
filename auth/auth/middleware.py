from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework.authentication import get_authorization_header
from django.conf import settings


class InternalAPIMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith('/i/'):
            auth = get_authorization_header(request).decode()
            if auth != settings.SECRET_KEY:
                return HttpResponse('Forbidden', status=403)
