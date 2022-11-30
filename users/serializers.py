from rest_framework import serializers
from .models import AuthUser, NormalUser, PremiumPlan



class PremiumPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumPlan
        fields = '__all__'

class AuthUserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'

class AuthUserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['email', 'avatar', 'password']

class NormalUserReadSerializer(serializers.ModelSerializer):
    premium_plan = PremiumPlanSerializer()
    class Meta(AuthUserReadSerializer.Meta):
        model = NormalUser
        fields = AuthUserReadSerializer.Meta.fields + NormalUser.DEFAULT_FIELDS

class NormalUserWriteSerializer(serializers.ModelSerializer):
    premium_plan = serializers.PrimaryKeyRelatedField(required=False)
    class Meta(AuthUserWriteSerializer.Meta):
        model = NormalUser
        fields = AuthUserWriteSerializer.Meta.fields + NormalUser.DEFAULT_FIELDS
