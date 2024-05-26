from rest_framework.views import APIView
from rest_framework.response import Response

from api.authentication import CustomOAuth2Authentication
from api.permission import CustomPermission

class SecureView(APIView):
    authentication_classes = [CustomOAuth2Authentication]
    permission_classes = [CustomPermission]

    def get(self, request):
        return Response({"message": "Hello, you have passed custom authentication and permission checks!"})
