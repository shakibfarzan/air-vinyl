from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class EncryptionPasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model: None

    def create(self, validated_data):
        """Create and return a superadmin with encrypted password."""
        validated_data["password"] = make_password(validated_data["password"])
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return superadmin."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

class ResponseSerializer(serializers.ModelSerializer):
    response_serializer: serializers.ModelSerializer = None

    def to_representation(self, instance):
        serializer = self.response_serializer(instance)
        return serializer.data