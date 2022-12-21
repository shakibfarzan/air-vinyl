from rest_framework import serializers
from airvinyl.utils.serializers import EncryptionPasswordSerializer, ResponseSerializer
from .models import AuthUser, NormalUser, PremiumPlan, SuperAdmin

class PremiumPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumPlan
        fields = '__all__'

class AuthUserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = AuthUser.READ_FIELDS

class AuthUserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = AuthUser.WRITE_FIELDS
        extra_kwargs = {'password': {'min_length': 8}}

class NormalUserReadSerializer(serializers.ModelSerializer):
    premium_plan = PremiumPlanSerializer()
    class Meta(AuthUserReadSerializer.Meta):
        model = NormalUser
        fields = AuthUserReadSerializer.Meta.fields + NormalUser.DEFAULT_FIELDS

class NormalUserWriteSerializer(EncryptionPasswordSerializer, ResponseSerializer):
    response_serializer = NormalUserReadSerializer
    premium_plan = serializers.PrimaryKeyRelatedField(required=False, queryset=PremiumPlan.objects.all())
    class Meta(AuthUserWriteSerializer.Meta):
        model = NormalUser
        fields = AuthUserWriteSerializer.Meta.fields + NormalUser.DEFAULT_FIELDS

class SuperAdminReadSerializer(serializers.ModelSerializer):
    class Meta(AuthUserReadSerializer.Meta):
        model = SuperAdmin
        
class SuperAdminWriteSerializer(EncryptionPasswordSerializer, ResponseSerializer):
    response_serializer = SuperAdminReadSerializer
    class Meta(AuthUserWriteSerializer.Meta):
        model = SuperAdmin

