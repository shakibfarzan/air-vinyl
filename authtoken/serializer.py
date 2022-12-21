from django.forms import CharField, ValidationError
from rest_framework import serializers
from users.models import AuthUser
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as JwtTokenObtainPairSerializer

class TokenObtainPairSerializer(JwtTokenObtainPairSerializer):
    username_field = get_user_model().USERNAME_FIELD

# class CustomJWTSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         credentials = {
#             'username': '',
#             'password': attrs.get("password")
#         }

#         # This is answering the original question, but do whatever you need here. 
#         # For example in my case I had to check a different model that stores more user info
#         # But in the end, you should obtain the username to continue.
#         user_obj = AuthUser.objects.filter(email=attrs.get("username")).first() or AuthUser.objects.filter(username=attrs.get("username")).first()
#         if user_obj:
#             credentials['username'] = user_obj.username

#         return super().validate(credentials)

# class MyTokenObtainSerializer(serializers.ModelSerializer):
#     username_field = AuthUser.email
    
#     def __init__(self, *args, **kwargs):
#         super(MyTokenObtainSerializer).__init__(*args, **kwargs)
        
#         self.fields[self.username_field] = CharField()
#         self.fields['password'] = PasswordField()
    
#     def validate(self, attrs):
#         self.user = AuthUser.objects.filter(email=attrs[self.username_field]).first()
        
#         if not self.user:
#             raise ValidationError('The user is not valid')
#         else:
#             if not self.user.check_password(attrs['password']):
#                 raise ValidationError('Incorrect password.')   
        
#         # if self.user is None or not self.user.is_active:
#         #     raise ValidationError('Account is not active')
             
#         return super().validate(attrs)
    
# class MyTokenObtainPairSerializer(MyTokenObtainSerializer):
#     @classmethod
#     def get_token(cls, user):
#         return RefreshToken.for_user(user)