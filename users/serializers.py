from rest_framework import serializers
from django.contrib.auth.hashers import make_password
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

class NormalUserReadSerializer(serializers.ModelSerializer):
    premium_plan = PremiumPlanSerializer()
    class Meta(AuthUserReadSerializer.Meta):
        model = NormalUser
        fields = AuthUserReadSerializer.Meta.fields + NormalUser.DEFAULT_FIELDS

class NormalUserWriteSerializer(serializers.ModelSerializer):
    premium_plan = serializers.PrimaryKeyRelatedField(required=False, queryset=PremiumPlan.objects.all())
    class Meta(AuthUserWriteSerializer.Meta):
        model = NormalUser
        fields = AuthUserWriteSerializer.Meta.fields + NormalUser.DEFAULT_FIELDS
        extra_kwargs = {'password': {'min_length': 8}}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        validated_data["password"] = make_password(validated_data["password"])
        return NormalUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

class SuperAdminReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperAdmin
        fields = AuthUserReadSerializer.Meta.fields
        
class SuperAdminWriteSerializer(serializers.ModelSerializer):
    class Meta(AuthUserWriteSerializer.Meta):
        model = SuperAdmin
        fields = AuthUserWriteSerializer.Meta.fields
        extra_kwargs = {'password': {'min_length': 8}}

    def create(self, validated_data):
        """Create and return a superadmin with encrypted password."""
        validated_data["password"] = make_password(validated_data["password"])
        return SuperAdmin.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return superadmin."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user