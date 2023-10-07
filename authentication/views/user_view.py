from rest_framework.permissions import AllowAny
from authentication.models import AuthUser
from authentication.serializers.user_serializer import RegisterSerializer
from authentication.serializers.CustomTokenObtainPairSerializer import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics


class UserRegistration(generics.CreateAPIView):
    queryset = AuthUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UserLogin(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
