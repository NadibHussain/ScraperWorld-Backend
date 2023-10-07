from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from authentication.models.custom_users import user_model
from authentication.models.users import AuthUser


class RegisterSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=15,
                                         validators=[UniqueValidator(
                                             queryset=AuthUser.objects.filter(is_active=True))])
    password = serializers.CharField(min_length=6)
    name = serializers.CharField(required=False, max_length=50)

    class Meta:
        model = AuthUser
        exclude = ('user_permissions','last_login','is_staff','is_superuser','groups','is_active' )
        extra_kwargs = {
            'password': {'write_only': True},
        }


