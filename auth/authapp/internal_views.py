from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView


class ValidateAuth(APIView):
    def post(self, request):
        try:
            user_id = Token.objects.values('user_id').get(key=request.data.get('token'))['user_id']
            return Response({'user_id': user_id})
        except Token.DoesNotExist:
            return Response('Unauthorized', 401)
