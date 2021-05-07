from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from rest_framework.authentication import get_authorization_header

from xo.services.internal_service import validate_user_auth, parse_authorization_header


class InternalAuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        token = parse_authorization_header(get_authorization_header(request))
        if token:
            user_id = validate_user_auth(token)
            if user_id != -1:
                setattr(request, 'user_id', user_id)
