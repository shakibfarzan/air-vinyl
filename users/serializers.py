from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import AuthUser, NormalUser, PremiumPlan

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
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
