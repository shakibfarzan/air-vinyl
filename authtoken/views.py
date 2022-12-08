from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from authtoken.serializer import TokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

