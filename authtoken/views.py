from rest_framework.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from authtoken.serializer import TokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    permission_class = TokenObtainPairSerializer

