from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from spotifyapp.utils.serializers import EncryptionPasswordSerializer
from .models import AuthUser, NormalUser, PremiumPlan, SuperAdmin

class PremiumPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumPlan
        fields = '__all__'

class AuthUserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['id', 'email', 'role', 'created_at', 'avatar']

class AuthUserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['email', 'avatar', 'password']
        extra_kwargs = {'password': {'min_length': 8}}

class NormalUserReadSerializer(serializers.ModelSerializer):
    premium_plan = PremiumPlanSerializer()
    class Meta(AuthUserReadSerializer.Meta):
        model = NormalUser
        fields = AuthUserReadSerializer.Meta.fields + NormalUser.DEFAULT_FIELDS

class NormalUserWriteSerializer(EncryptionPasswordSerializer):
    premium_plan = serializers.PrimaryKeyRelatedField(required=False, queryset=PremiumPlan.objects.all())
    class Meta(AuthUserWriteSerializer.Meta):
        model = NormalUser
        fields = AuthUserWriteSerializer.Meta.fields + NormalUser.DEFAULT_FIELDS

class SuperAdminReadSerializer(serializers.ModelSerializer):
    class Meta(AuthUserReadSerializer.Meta):
        model = SuperAdmin
        
class SuperAdminWriteSerializer(EncryptionPasswordSerializer):
    class Meta(AuthUserWriteSerializer.Meta):
        model = SuperAdmin

