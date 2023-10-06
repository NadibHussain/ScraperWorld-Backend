from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authentication.models import AuthUser

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user: AuthUser):
        token = super().get_token(user)

        token['name'] = user.name
        token['email'] = user.email
        token['user_id'] = user.id
        token['is_superuser'] = user.is_superuser
        return token
